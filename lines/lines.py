import sys
l=0
try:
    if sys.argv[1].endswith(".py") and sys.argv[2].endswith(".py") :
        print("Too many command-line arguments")
        sys.exit
    elif not(sys.argv[1].endswith(".py")):
        print("Not a python file")
        sys.exit
    with open(sys.argv[1]) as file:
        for line in file:
            if line.startswith("# ") or line.isspace():
                continue
            l=l+1
    print(l)
except IndexError:
    print("Too few command-line arguments")
    sys.exit
except FileNotFoundError:
    print("File does not exist")
    sys.exit




