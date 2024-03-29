import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    link=re.search(r"^<\w+ \w+=\"\w+://(\w+\.\w+\.\w+)/\w+/(\w+)\"></\w+>$",s)
    if link.group(1)!="www.youtube.com":
        return "None"
    watchlink="htpps://youtu.be/"+link.group(2)
    return watchlink


if __name__ == "__main__":
    main()
