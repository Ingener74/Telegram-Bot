# encoding: utf8
import json

__author__ = 'pavel'

from JsonPickle import (JsonPickle)

class Message(JsonPickle):
    def __init__(self, jobj):
        self.message_id = jobj[]

    def to_json(self):
        return json.load('{}')