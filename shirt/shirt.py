import sys
def main():
    if len(sys.argv)<2:
        sys.exit("Too few command line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too many command line arguments")
    else:
        if not(sys.argv[1].endswith(".jpg") and sys.argv[2].endswith(".jpg")):
            sys.exit("Invalid input")
        if check_extension():
            sys.exit("Input and output have different extensions")


def check_extension():
    end1=sys.argv[1][-4]
    end2=sys.argv[2][-4]
    if end1==end2:
        return False
    else:
        return True
def check_valid():
    end1=sys.argv[1][-4]
    end2=sys.argv[2][-4]
    if end1==".jpg" or end2=".jpg":
        

