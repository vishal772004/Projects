import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if time:=re.search("^[0-9]+(:[0-9]+) (AM|PM)+ to [0-9]+(:[0-9]+) (AM|PM)+$",s):
        li=s.split(" to ")
        



if __name__ == "__main__":
    main()
