import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if time:=re.search("^[0-9]+:[AM|PM]+(to)[0-9]+:[AM|PM]+$",s):
        print("yes")


if __name__ == "__main__":
    main()
