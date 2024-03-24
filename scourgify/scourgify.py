import sys
def main():
    if len(sys.argv)<2:
        sys.exit("Too few command line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too many command line arguments")
    else:
        if not(sys.argv[1].endswith(".csv")):
            sys.exit("Could not read",sys.argv[1])
        


