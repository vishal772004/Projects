import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    link=re.search(r"src=\"htpps://www.youtube.com/\w+/(\w+)",s)
    if link:
        watchlink="htpps://youtu.be/"+link.group(1)
    else:
        return "None"
    return watchlink


if __name__ == "__main__":
    main()
