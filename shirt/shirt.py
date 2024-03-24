import sys
from PIL import Image
def main():
    if len(sys.argv)<3:
        sys.exit("Too few command line arguments")
    elif len(sys.argv)>3:
        sys.exit("Too many command line arguments")
    else:
        try:
            if check_valid():
                sys.exit("Invalid input")
            if check_extension():
                sys.exit("Input and output have different extensions")
            shirt = Image.open(sys.argv[1])
            size = sys.argv[1].size
            sys.argv[2].paste(shirt, "shirt.png")
        except FileNotFoundError:
            sys.exit("Input Does not exist")

def check_extension():
    end1=sys.argv[1][-4]
    end2=sys.argv[2][-4]
    if end1==end2:
        return False
    else:
        return True
def check_valid():
    if sys.argv[1].endswith(".jpg") or sys.argv[1].endswith(".png"):
        pass
    elif sys.argv[2].endswith(".jpg") or sys.argv[2].endswith(".png"):
        return False
    else:
        return True

if __name__=="__main__":
    main()
