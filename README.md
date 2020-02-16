##**A Simple Calculator Project**


In this project, i used a *Fire* to solve expressions such as BODMAS,which solves multiple operations i.e addition,subtraction,multiplication and division. Where *fire* is a Python library that will turn any Python component into a command line interface with just a single call to Fire.

**Getting Started**

To install Python Fire from pypi, run:
> pip install fire

Alternatively, to install Python Fire from source, clone the source and run:
> python setup.py install

The easiest way to use *Fire* is to take any Python program, and then simply call fire.Fire() at the end of the program. This will expose the full contents of the program to the command line.

**Example**
```
import fire

def hello(name):
  return 'Hello {name}!'.format(name=name)

if __name__ == '__main__':
  fire.Fire()
```
Here's how we can run our program from the command line:
```
$ python example.py hello World
Hello World!
```
Just like above example,i have written the code which is then called by solve.
```
fire.Fire()
Turns the current module into a Fire CLI.
```
```
fire.Fire(component)
Turns component into a Fire CLI.
```
at the end,run
```
calci solve 2+3*5/1
```
