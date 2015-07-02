# encoding: utf8
import json
from unittest import TestCase
from TelegramBot.User import User

__author__ = 'pavel'


class TestUser(TestCase):
    def test_to_json(self):
        user = User(42, 'Pavel', 'Shnaider', 'Username42')
        self.assertEqual(json.load('{"id":42, "first_name":"Pavel", "last_name":"Shnaider", "username":"Username42"}'),
                         user.to_json())

if __name__ == '__main__':
    unittest.main()