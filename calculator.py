import fire

class Calculator(object):

  def add(self, x, y):
    return x + y 

  def sub(self, x, y):
    return x - y

  def div(self, x, y):
    return x / y

  def multiply(self, x, y):
    return x * y

  def mod(self, x, y):
    return x % y

  def double(self, x):
    return 2 * x

if __name__ == '__main__':
  calculator = Calculator()
  fire.Fire(calculator)

