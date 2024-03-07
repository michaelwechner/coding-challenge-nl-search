from swagger_server.models.search_output import SearchOutput  # noqa: E501

from flask import jsonify
from swagger_server.models.hit import Hit
from swagger_server.services.datarepository import DataRepository


def api_v1_search_get(query):  # noqa: E501
    """Returns answer to asked question including document store IDs, which contain text the answer is based on

     # noqa: E501

    :param query: Question, e.g. &#x27;When was Michael born?&#x27;
    :type query: str

    :rtype: SearchOutput
    """

    hits = DataRepository().search(query=query)


    #hit1 = Hit('Michael was born 1969', 0.8689, 56)
    #hit2 = Hit('Michael was born in St. Gallen', 0.5427, 34)
    #hit3 = Hit('Vanya was born 2001', 0.2677, 17)
    #hits = [hit1, hit2, hit3]
    ##hits = [hit1.text, hit2.text, hit3.text]

    # TODO: Use completion to generate answer: https://github.com/openai/openai-python

    response = {'query': query, 'llm': 'TODO: For example Mistral', 'results': hits}
    return jsonify(response)
