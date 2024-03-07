# AI Service

import uuid

import os

from astrapy.db import AstraDB
from swagger_server.services.ai import AI
from swagger_server.models.hit import Hit

class DataRepository(dict):
    def __init__(self):
        #token=os.environ["ASTRA_DB_APPLICATION_TOKEN"]
        #token=os.environ.get("ASTRA_DB_APPLICATION_TOKEN")
        token=os.getenv("ASTRA_DB_APPLICATION_TOKEN")
        print(f"Token: {token}")

        #api_endpoint=os.environ["ASTRA_DB_API_ENDPOINT"]
        #api_endpoint=os.environ.get("ASTRA_DB_API_ENDPOINT")
        api_endpoint=os.getenv("ASTRA_DB_API_ENDPOINT")
        print(f"API Endpoint: {api_endpoint}")

        # TODO: Singleton
        self.db = AstraDB(
            token=os.getenv("ASTRA_DB_APPLICATION_TOKEN"),
            api_endpoint=os.getenv("ASTRA_DB_API_ENDPOINT"),
            namespace="default_keyspace",
        )
        print(self.db)

        db_collection_name=os.getenv("ASTRA_DB_COLLECTION")
        print(f"DB Collection Name: {db_collection_name}")

        self.collection = self.db.collection(db_collection_name)

    def memorizeText(self, text: str):
        print(f"Insert text: {text}")
        id = str(uuid.uuid4())

        embedding = AI().getEmbedding(text, input_type="search_document")
        print(f"Vector embedding dimension: {len(embedding)}")

        documents = [{"_id": id,"text": text, "$vector": embedding}]
        print(f"Insert document(s): {documents}")
        res = self.collection.insert_many(documents)

        return id

    def getText(self, id_: str):
        print(f"Get document {id_} ...")
        results = self.collection.find({"_id": id_})
        chunks = []
        for document in results["data"]["documents"]:
            print(document['text'])
            chunks.append(document['text'])

        return chunks

    def search(self, query: str):
        print(f"Get embedding for query text '{query}' ...")
        query_embedding = AI().getEmbedding(text=query, input_type="search_query")
        print(f"Query embedding: {query_embedding}")

        db_results = self.collection.vector_find(vector=query_embedding, limit=10)
        hits = []
        for document in db_results:
            print(f"Found document: {document}")
            hit = Hit(document['text'], document['$similarity'], document['_id'])
            hits.append(hit)

        return hits

