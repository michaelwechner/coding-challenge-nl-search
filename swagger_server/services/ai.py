# AI Service

import os

from openai import OpenAI
from cohere import Client

class AI(dict):
    def __init__(self):
        # TODO: Singleton
        self.cohere = Client(api_key=os.environ.get("COHERE_API_KEY"))

    def getEmbedding(self, text: str, input_type: str="search_document"):
        # TODO: Make embedding model 'text-embedding-ada-002' or 'embed-multilingual-v3.0' configurable

        # INFO: Cohere implementation
        texts = [text]
        #texts = [text, "Hello World"]
        print(f"Get embeddings for texts '{texts}' ...")
        # https://cohere-sdk.readthedocs.io/en/latest/cohere.html#cohere.client.Client.embed resp. https://docs.cohere.com/reference/embed
        embeddings = self.cohere.embed(texts=texts, model="embed-multilingual-v2.0") # Length: 768
        #embeddings = self.cohere.embed(texts=texts, model="embed-multilingual-v2.0") # Length: 768
        #print(f"Cohere Embeddings: {embeddings}")
        embedding = embeddings.embeddings[0]

        # INFO: OpenAI implementation
        #client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        #embedding = client.embeddings.create(input=body.text, model="text-embedding-ada-002")

        # INFO: Mock implementation
        #embedding = [0.1, 0.15, 0.3, 0.12, 0.05]

        return embedding
