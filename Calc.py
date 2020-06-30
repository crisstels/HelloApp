class Calculator():
    '''Submits two numbers and returns the sum.'''

    def post(self, numbers):
        return {'sum': numbers['num1'] + numbers['num2']}
