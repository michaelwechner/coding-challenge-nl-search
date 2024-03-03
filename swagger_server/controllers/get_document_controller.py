import connexion
import six
import os

from swagger_server.models.get_document_output import GetDocumentOutput  # noqa: E501
from swagger_server import util

from flask import jsonify
from swagger_server.models.chunk import Chunk
from astrapy.db import AstraDB


def api_v1_documents_id_get(id_):  # noqa: E501
    """Returns content of a particular document from document store

     # noqa: E501

    :param id_: ID of document
    :type id_: str

    :rtype: GetDocumentOutput
    """

    db = AstraDB(
        token=os.getenv("ASTRA_DB_APPLICATION_TOKEN"),
        api_endpoint=os.getenv("ASTRA_DB_API_ENDPOINT"),
        namespace="default_keyspace",
    )
    print(db)

    db_collection_name=os.getenv("ASTRA_DB_COLLECTION")
    print(f"DB Collection Name: {db_collection_name}")

    collection = db.collection(db_collection_name)
    print(f"Get document {id_} ...")
    results = collection.find({"_id": id_})
    for document in results["data"]["documents"]:
        print(document)

    chunk1 = Chunk('Michael was born 1969')
    chunk2 = Chunk('Michael was born in St. Gallen')
    chunks = [chunk1, chunk2]

    response = {'id': id_, 'chunks': chunks}
    return jsonify(response)
