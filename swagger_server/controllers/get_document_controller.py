import connexion
import six

from swagger_server.models.get_document_output import GetDocumentOutput  # noqa: E501
from swagger_server import util

from flask import jsonify
from swagger_server.models.chunk import Chunk


def api_v1_documents_id_get(id_):  # noqa: E501
    """Returns content of a particular document from document store

     # noqa: E501

    :param id_: ID of document
    :type id_: int

    :rtype: GetDocumentOutput
    """

    chunk1 = Chunk('Michael was born 1969')
    chunk2 = Chunk('Michael was born in St. Gallen')
    chunks = [chunk1, chunk2]

    response = {'id': id_, 'chunks': chunks}
    return jsonify(response)
