# Search Result Hit

import json

class Hit(dict):
    def __init__(self, text: str=None, score: float=None, id: int=None):
        dict.__init__(self, text=text, score=score, id=id)
        self.text = text
        self.score = score
        self.id = id

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
