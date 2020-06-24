'''REST Interface to add up two numbers '''
from flask import Flask
from flask import request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    '''Submits two numbers and the retrieve them back'''

    def get(self, number1):
        return {'number1': number1}

    def post(self):
        number1 = request.form['data']
        return {'number1': number1}

    @staticmethod
    def get(number2):
        return {'number2': number2}

    def post(self):
        number2 = request.form['number']
        return {'number2': number2}


api.add_resource(HelloWorld, "/")

if __name__ == "__main__":
    app.run(debug=True)
