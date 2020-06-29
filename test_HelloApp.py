''' Unit test for HelloApp.py application'''
import json
import unittest

import requests

from HelloApp import app


class TestFlask(unittest.TestCase):

    # # check response
    # def test_index(self):
    #     tester = app.test_client(self)
    #     response = tester.get("/sum")
    #     statuscode = response.status_code
    #     self.assertEqual(statuscode, 405)

    # check if content return is application/json
    def test_content(self):
        tester = app.test_client(self)
        response = tester.get("/sum")
        self.assertEqual(response.content_type, "application/json")

    # check for data returned
    def test_post(self, mock_post):
        info = {"num1": 1, "num2": 1}
        resp = requests.post("http://127.0.0.1:5000/", data=json.dumps(info),
                             headers={'Content-Type': 'application/json'})
        mock_post.assert_called_with("http://127.0.0.1:5000/", data=json.dumps(info),
                                     headers={'Content-Type': 'application/json'})


if __name__ == "__main__":
    if __name__ == '__main__':
        unittest.main()
