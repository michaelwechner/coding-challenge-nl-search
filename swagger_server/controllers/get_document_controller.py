import connexion
import six

from swagger_server.models.get_document_output import GetDocumentOutput  # noqa: E501
from swagger_server import util


def api_v1_documents_id_get(id):  # noqa: E501
    """Returns content of a particular document from document store

     # noqa: E501

    :param id: ID of document
    :type id: int

    :rtype: GetDocumentOutput
    """
    return 'do some magic!'
