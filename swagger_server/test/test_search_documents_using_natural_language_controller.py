# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.search_output import SearchOutput  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSearchDocumentsUsingNaturalLanguageController(BaseTestCase):
    """SearchDocumentsUsingNaturalLanguageController integration test stubs"""

    def test_api_v1_search_get(self):
        """Test case for api_v1_search_get

        Returns answer to asked question including document store IDs, which contain text the answer is based on
        """
        query_string = [('query', 'query_example')]
        response = self.client.open(
            '/api/v1/search',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
