import fire

class Calculator(object):

  def add(self, x, y):
      value = x + y
      number = int(input("enter a no: "))
      result = value + number
      return result

  def multiply(self, x, y):
      value = x * y
      number = int(input("enter a no: "))
      result = value * number
      return result

  def div(self, x, y):
      value = x / y
      number = int(input("enter a no: "))
      result = value / number
      return result

  def sub(self, x, y):
      value = x - y
      number = int(input("enter a no: "))
      result = value - number
      return result

  def solve(self, p):
      evaluate = p
      expression = eval(evaluate)
      print(expression)
      print(type(expression))

