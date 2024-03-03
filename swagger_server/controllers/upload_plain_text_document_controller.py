import connexion
import six
import os
import uuid

from swagger_server.models.upload_document_input import UploadDocumentInput  # noqa: E501
from swagger_server.models.upload_document_output import UploadDocumentOutput  # noqa: E501
from swagger_server import util

from flask import jsonify
from astrapy.db import AstraDB
from openai import OpenAI
from cohere import Client


def api_v1_documents_post(body=None):  # noqa: E501
    """Returns newly created store ID of uploaded document

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: UploadDocumentOutput
    """
    if connexion.request.is_json:
        body = UploadDocumentInput.from_dict(connexion.request.get_json())  # noqa: E501

    #token=os.environ["ASTRA_DB_APPLICATION_TOKEN"]
    #token=os.environ.get("ASTRA_DB_APPLICATION_TOKEN")
    token=os.getenv("ASTRA_DB_APPLICATION_TOKEN")
    print(f"Token: {token}")

    #api_endpoint=os.environ["ASTRA_DB_API_ENDPOINT"]
    #api_endpoint=os.environ.get("ASTRA_DB_API_ENDPOINT")
    api_endpoint=os.getenv("ASTRA_DB_API_ENDPOINT")
    print(f"API Endpoint: {api_endpoint}")

    db_collection_name=os.getenv("ASTRA_DB_COLLECTION")
    print(f"DB Collection Name: {db_collection_name}")

    db = AstraDB(
        token=token,
        api_endpoint=api_endpoint,
        namespace="default_keyspace",
    )
    print(db)

    print(f"Insert text: {body.text}")
    id = str(uuid.uuid4())

    # TODO: Make embedding model 'text-embedding-ada-002' or 'embed-multilingual-v3.0' configurable

    # https://cohere-sdk.readthedocs.io/en/latest/cohere.html#cohere.client.Client.embed resp. https://docs.cohere.com/reference/embed
    cohere = Client(api_key=os.environ.get("COHERE_API_KEY"))
    texts=[body.text]
    #texts=[body.text, "Hello World"]
    embeddings = cohere.embed(texts=texts, model="embed-multilingual-v2.0") # Length: 768
    #embeddings = cohere.embed(texts=texts, model="embed-multilingual-v3.0", input_type="search_document") # Length: 1024
    print(f"Cohere Embeddings: {embeddings}")
    embedding = embeddings.embeddings[0]
    print(f"Vector embedding dimension: {len(embedding)}")

    #client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    #embedding = client.embeddings.create(input=body.text, model="text-embedding-ada-002")

    #embedding = [0.1, 0.15, 0.3, 0.12, 0.05]

    documents = [{"_id": id,"text": body.text, "$vector": embedding}]
    print(f"Insert document(s): {documents}")
    collection = db.collection(db_collection_name)
    res = collection.insert_many(documents)

    response = {'id': id}
    return jsonify(response)
