#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div

operators = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': div
}

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator = sys.argv[2]

        if operator not in operators:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)

        result = operators[operator](a, b)
        print("{} {} {} = {}".format(a, operator, b, result))
