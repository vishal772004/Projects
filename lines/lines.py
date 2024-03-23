import sys
def main():
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    l=0
    try:
        if not(sys.argv[1].endswith(".py")):
            sys.exit("Not a python file")
        with open(sys.argv[1]) as file:
            lines=file.readlines()
        for line in lines:
            if line.startswith("#") or line.isspace():
                continue
            l=l+1
        print(lines)
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__=="__main__":
    main()



