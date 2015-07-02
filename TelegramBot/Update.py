# encoding: utf8
__author__ = 'pavel'
import json
from JsonPickle import (JsonPickle)
from Message import (Message)

class Update(JsonPickle):
    def __init__(self, jobj):
        self.update_id = jobj['update_id']
        self.message = Message(jobj['message'])

    def to_json(self):
        return json.load('{"update_id":' + self.update_id + ', "message": ' + self.message.to_json() + '}')