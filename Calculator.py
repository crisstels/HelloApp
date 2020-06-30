'''REST Interface to add up two numbers. Use the
curl -H "Content-Type: application/json" -X POST -d '{"num1": 1, "num2": 1}' http://127.0.01:5000/
command to test it.'''
from flask import Flask
from flask import request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Calculator(Resource):
    '''Submits two numbers and returns the sum.'''

    def post(self):
        numbers = request.get_json()
        return {'sum': numbers['num1'] + numbers['num2']}


api.add_resource(Calculator, "/sum")

if __name__ == "__main__":
    app.run()
