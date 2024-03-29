import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    link=re.search(r"^<\w+ \w+=\"\w+://\w+\.\w+\.\w+/\w+/(\w+)\"></\w+>$",s)
    


if __name__ == "__main__":
    main()
