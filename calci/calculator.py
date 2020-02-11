import fire

class Calculator(object):

  def add(x, y):
    result = x + y
    value = int(input( 'enter the value:' ))
    number = result + value
    return number

  def multiply(x, y):
    result = x * y
    value = int(input( 'enter the value:' ))
    number = result * value
    return number

  def division(x, y):
    result = x / y
    value = int(input( 'enter the value:' ))
    number = result / value
    return number

  def subtract(x, y):
    result = x - y
    value = int(input( 'enter the value:' ))
    number = result - value
    return number
