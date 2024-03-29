import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    link=re.search(r"^<\w+ \w+=\"\w+://\w+\.\w+\.\w+/\w+/(\w+)\"></\w+>$",s)
    watchlink="htpps://youtu.be/"+link.group(1)
    return watchlink


if __name__ == "__main__":
    main()
