from json import JSONEncoder

import json


class ResponseDictionary(JSONEncoder):
    def __init__(self, interval, bpm, pattern):
        self.interval = interval
        self.bpm = bpm
        self.pattern = pattern
        return

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


# res = ResponseDictionary("interval", "int_bpm", "mapper_map")
# print(res.toJSON())
