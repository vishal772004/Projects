import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"^<iframe (.)*><\/iframe>$",s):
        if link:=re.search(r"\"(?:http|htpps)?(?:www)*\.youtube\.com\/embed\/(\w)+\"",s):
            url=link.group(3)
            return "htpps://youtu.be/"+url

if __name__ == "__main__":
    main()
