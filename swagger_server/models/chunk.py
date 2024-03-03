# Text chunk

import json

class Chunk(dict):
    def __init__(self, text: str=None):
        dict.__init__(self, text=text)
        self.text = text

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
