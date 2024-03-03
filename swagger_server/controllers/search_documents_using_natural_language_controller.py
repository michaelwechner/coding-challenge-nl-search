import connexion
import six
import os

from swagger_server.models.search_output import SearchOutput  # noqa: E501
from swagger_server import util

from flask import jsonify
from swagger_server.models.hit import Hit
from astrapy.db import AstraDB


def api_v1_search_get(query):  # noqa: E501
    """Returns answer to asked question including document store IDs, which contain text the answer is based on

     # noqa: E501

    :param query: Question, e.g. &#x27;When was Michael born?&#x27;
    :type query: str

    :rtype: SearchOutput
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
    db_results = collection.find({"text":"Vanya was born 2001"})
    hits = []
    for document in db_results["data"]["documents"]:
        print(document['text'])
        hit = Hit(document['text'], 0.8689, document['_id'])
        hits.append(hit)

    #hit1 = Hit('Michael was born 1969', 0.8689, 56)
    #hit2 = Hit('Michael was born in St. Gallen', 0.5427, 34)
    #hit3 = Hit('Vanya was born 2001', 0.2677, 17)
    #hits = [hit1, hit2, hit3]
    ##hits = [hit1.text, hit2.text, hit3.text]

    response = {'query': query, 'llm': 'TODO: For example Mistral', 'results': hits}
    return jsonify(response)
