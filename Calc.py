class Calculator():
    '''Submits two numbers and returns the sum.'''
    def post(self, numbers):
        if not (type(numbers['num1']) is int) and not (type(numbers['num2'] is int)):
            raise TypeError("Only integers are allowed!")

        return {'sum': numbers['num1'] + numbers['num2']}
