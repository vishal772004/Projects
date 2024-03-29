import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    link=re.search(r"src=\"htpps://(www.youtube.com)/\w+/(\w+)",s)
    watchlink="htpps://youtu.be/"+link.group(2)
    return watchlink


if __name__ == "__main__":
    main()
