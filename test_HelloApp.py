''' Unit test for HelloApp.py application'''
import json
import unittest
from unittest.mock import patch

import requests

from HelloApp import app


class TestFlask(unittest.TestCase):

    # check if content return is application/json
    def test_content(self):
        tester = app.test_client(self)
        response = tester.get("/sum")
        self.assertEqual(response.content_type, "application/json")

    # checks returned data
    def test_post(self, mock_post):
        info = {"num1": 1, "num2": 1}
        resp = requests.post("http://127.0.01:5000/sum", data=json.dumps(info),
                             headers={'Content type': 'application/json'})
        mock_post.assert_called_with("http://127.0.0.1:5000/sum", data=json.dumps(info),
                                     headers={'Content type': 'application/json'})

    # def test_Calculator(self):
    #
    #     calculator = Calculator()
    #     output = {'sum': 7}
    #
    #     result = calculator.post()
    #     self.assertEqual(output, result)


if __name__ == "__main__":
    unittest.test_post(patch)
