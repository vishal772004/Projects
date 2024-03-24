import sys
def main():
    if len(sys.argv)<2:
        sys.exit("Too few command line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too many command line arguments")
    else:
        if sys.argv[1].endswith(".jpg") and sys.argv[2].endswith(".jpg"):
            sys.exit("Invalid input")

        if not(sys.argv[1].endswith(".jpg") and sys.argv[2].endswith(".jpg")):
            sys.exit("Input and output have different extensions")

