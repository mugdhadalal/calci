import fire
from calci.calculator import Calculator

def main():
    calculator = Calculator()
    fire.Fire(Calculator)


if __name__ == '__main__':
    main()
