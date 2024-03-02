# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.upload_document_input import UploadDocumentInput  # noqa: E501
from swagger_server.models.upload_document_output import UploadDocumentOutput  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUploadPlainTextDocumentController(BaseTestCase):
    """UploadPlainTextDocumentController integration test stubs"""

    def test_api_v1_documents_post(self):
        """Test case for api_v1_documents_post

        Returns newly created store ID of uploaded document
        """
        body = UploadDocumentInput()
        response = self.client.open(
            '/api/v1/documents',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
