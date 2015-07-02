# encoding: utf8
import json
import urllib
import urllib2


class Bot(object):
    API = 'https://api.telegram.org/bot'

    def __init__(self, token):
        self.url = Bot.API + token

    def sendMessage(self, chat_id, text):
        query = {'chat_id': chat_id,'text': text}
        get = self.url + '/sendMessage?' + urllib.urlencode(query)
        response = urllib2.urlopen(get)
        self.checkResponse(response)

    def checkResponse(self, response):
        res_js = json.load(response)
        if not res_js['ok']:
            raise RuntimeError('checkResponse error')
