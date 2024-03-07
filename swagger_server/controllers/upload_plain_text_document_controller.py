import connexion

from swagger_server.models.upload_document_input import UploadDocumentInput  # noqa: E501
from swagger_server.models.upload_document_output import UploadDocumentOutput  # noqa: E501

from flask import jsonify
from swagger_server.services.datarepository import DataRepository


def api_v1_documents_post(body=None):  # noqa: E501
    """Returns newly created store ID of uploaded document

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: UploadDocumentOutput
    """
    if connexion.request.is_json:
        body = UploadDocumentInput.from_dict(connexion.request.get_json())  # noqa: E501

    id = DataRepository().memorizeText(text=body.text)

    response = {'id': id}
    return jsonify(response)
