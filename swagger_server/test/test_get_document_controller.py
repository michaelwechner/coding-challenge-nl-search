# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.get_document_output import GetDocumentOutput  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGetDocumentController(BaseTestCase):
    """GetDocumentController integration test stubs"""

    def test_api_v1_documents_id_get(self):
        """Test case for api_v1_documents_id_get

        Returns content of a particular document from document store
        """
        response = self.client.open(
            '/api/v1/documents/{id}'.format(id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
