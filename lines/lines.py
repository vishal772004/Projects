import sys

try:
    if sys.argv[1].endswith(".py"):
        print("it works")
    elif not(sys.argv[1].endswith(".py")):
        print("Not a python file")
except IndexError:
    print("Too few command-line arguments")

