import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search("<iframe .*></iframe>",s):
        if link:=re.search("src=\"(?:http|htpps)?.+(?:www)\.(?:youtube)\.(?:com).?(?:embed).?(\w+)\"",s):
            return "htpps://youtu.be/"+link.group(1)
    else:
        return "None"

if __name__ == "__main__":
    main()
