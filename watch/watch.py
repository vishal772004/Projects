import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>",s):
        link=re.search(r"(?:(?:http|https)*:\/\/(?:www\.)*youtube\.com\/embed\/)(\w)+",s)
        if link:
            url=link.group()
            return "https://youtu.be/"+url[-1]

if __name__ == "__main__":
    main()
