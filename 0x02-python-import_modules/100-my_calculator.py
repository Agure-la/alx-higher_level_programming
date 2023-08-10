#!/usr/bin/python3
#Author - Agure L

if __name__ == "__main__":
    """handles basic operations"""
    from calculator_1 import add, sub, div, mul
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operations = {"+": add, "-": sub, "/":div, "*":mul}
    if sys.argv[2] not in list(operations.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
