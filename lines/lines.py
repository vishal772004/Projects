import sys
l=0
try:
    if sys.argv[1].endswith(".py"):
        pass
    elif not(sys.argv[1].endswith(".py")):
        print("Not a python file")
    with open(sys.argv[1]) as file:
        for line in file:
            if line.startswith("# ") or line.isspace():
                continue
            l=l+1
    print(l)
except IndexError:
    print("Too few command-line arguments")
except FileNotFoundError:
    print("File does not exist")




