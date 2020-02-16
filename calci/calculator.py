import fire

class Calculator(object):


  def solve(self, p):
      evaluate = p
      expression = eval(evaluate)
      print(expression)
      print(type(expression))

