import connexion
import six
import os
import uuid

from swagger_server.models.upload_document_input import UploadDocumentInput  # noqa: E501
from swagger_server.models.upload_document_output import UploadDocumentOutput  # noqa: E501
from swagger_server import util

from flask import jsonify
from astrapy.db import AstraDB
from swagger_server.services.ai import AI


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

    embedding = AI.getEmbedding(body.text, input_type="search_document")
    print(f"Vector embedding dimension: {len(embedding)}")

    documents = [{"_id": id,"text": body.text, "$vector": embedding}]
    print(f"Insert document(s): {documents}")
    collection = db.collection(db_collection_name)
    res = collection.insert_many(documents)

    response = {'id': id}
    return jsonify(response)
