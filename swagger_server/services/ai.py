# AI Service

import os

from openai import OpenAI
from cohere import Client

class AI(dict):
    def __init__(self):
        # TODO: Singleton
        self.cohere = Client(api_key=os.environ.get("COHERE_API_KEY"))

    def getEmbedding(self, text: str=None, input_type: str="search_document"):
        # INFO: Cohere implementation
        texts = [text]
        #texts = [text, "Hello World"]
        cohere = Client(api_key=os.environ.get("COHERE_API_KEY"))
        embeddings = cohere.embed(texts=texts, model="embed-multilingual-v2.0") # Length: 768
        #embeddings = self.cohere.embed(texts=texts, model="embed-multilingual-v2.0") # Length: 768
        embedding = embeddings.embeddings[0]

        # INFO: Mock implementation
        #embedding = [0.1, 0.15, 0.3, 0.12, 0.05]

        return embedding
