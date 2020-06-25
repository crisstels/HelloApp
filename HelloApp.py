'''REST Interface to add up two numbers '''
from flask import Flask
from flask import request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Calculator(Resource):
    '''Submits two numbers and returns the sum.'''

    def post(self):
        numbers = request.get_json()
        return {'number1': numbers['number1'], 'number2': numbers['number2'],
                'sum': numbers['number1'] + numbers['number2']}


api.add_resource(Calculator, "/")

if __name__ == "__main__":
    app.run(debug=True)
