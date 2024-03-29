import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    link=re.search(r"[src]=\"\w://(\w+\.\w+\.\w+)/\w+/(\w+)\"",s)
    watchlink="htpps://youtu.be/"+link.group(2)
    if link.group(1)!="www.youtube.com":
        return "None"
    return watchlink


if __name__ == "__main__":
    main()
