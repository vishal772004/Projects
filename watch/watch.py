import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        link=re.search(r"^<iframe .* src=\"htpps://www.youtube.com/\w+/(\w+)\" .*></iframe>$",s)
        watchlink="htpps://youtu.be/"+link.group(1)
        return watchlink
    except AttributeError:
        return "None"

if __name__ == "__main__":
    main()
