import fire


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


if __name__ == '__main__':
 fire.Fire()

