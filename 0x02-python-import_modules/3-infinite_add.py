#!/usr/bin/python3
#Author Agure

if __name__ == "__main__":
    """prints the sum of all args"""
    import sys

    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
