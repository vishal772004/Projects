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
            image = Image.open(sys.argv[1])
            shirt = Image.open("shirt.png")
            size = shirt.size
            muppet=ImageOps.fit(image,size)
            muppet.paste(shirt,shirt)
            muppet.save(sys.argv[2])

        except FileNotFoundError:
            sys.exit("Input Does not exist")

def check_extension():
    if sys.argv[1].endswith(".jpg") and sys.argv[2].endswith(".jpg") :
        return False
    elif sys.argv[1].endswith(".png") and sys.argv[2].endswith(".png"):
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
