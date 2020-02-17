import fire


class Calculator(object):

    def solve(self, evaluate):
        expression = eval(evaluate)
        print(expression)
