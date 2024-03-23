import sys
l=0
check=0
try:

    if sys.argv[1].endswith(".py"):
        pass
    elif not(sys.argv[1].endswith(".py")):
        sys.exit("Not a python file")
    with open(sys.argv[1]) as file:
        for line in file:
            if line.startswith("# ") or line.isspace():
                continue
            l=l+1
    print(l)
except IndexError:
    if len(sys.argv)==3:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")
except FileNotFoundError:
    sys.exit("File does not exist")




