# encoding: utf8
__author__ = 'pavel'
import json
from JsonPickle import (JsonPickle)


class User(JsonPickle):
    def __init__(self, id, first_name, last_name='', username=''):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    def __init__(self, jobj):
        self.__init__(jobj['id'], jobj['first_name'], jobj['last_name'], jobj['username'])

    def to_json(self):
        return json.load('{"id":' + self.id +
                         ', "first_name":' + self.first_name +
                         ', "last_name": ' + self.last_name +
                         ', "username": ' + self.username +
                         '}')
