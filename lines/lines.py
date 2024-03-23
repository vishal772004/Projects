def main():
    import sys
    l=0
    try:
        if sys.argv[1].endswith(".py"):
            pass
        elif not(sys.argv[1].endswith(".py")):
            sys.exit("Not a python file")
        with open(sys.argv[1]) as file:
            lines=file.readlines()
        for line in lines:
            if line.startswith("#") or line.isspace():
                continue
            l=l+1
        if len(sys.argv)==3:
            sys.exit("Too many command-line arguments")
        print(l)
    except IndexError:
        sys.exit("Too few command-line arguments")
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__=="__main__":
    main()



