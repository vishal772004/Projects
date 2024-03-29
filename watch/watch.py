import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>",s):
        link=re.search(r"(?:http|https)*:\/\/(?:www\.)*youtube\.com\/embed\/(\w)+",s)
        if link:
            return "https://youtu.be/"+link.group(1)

if __name__ == "__main__":
    main()
