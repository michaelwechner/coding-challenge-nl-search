import connexion
import six

from swagger_server.models.search_output import SearchOutput  # noqa: E501
from swagger_server import util

from flask import jsonify


def api_v1_search_get(query):  # noqa: E501
    """Returns answer to asked question including document store IDs, which contain text the answer is based on

     # noqa: E501

    :param query: Question, e.g. &#x27;When was Michael born?&#x27;
    :type query: str

    :rtype: SearchOutput
    """

    response = {'query': query, 'llm':'TODO: For example Mistral', 'results':'[{id=5, score=0.8767, text=text}]'}
    return jsonify(response)
