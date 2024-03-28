import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ipv4=re.search(r"^(\d)\.(\d)\.(\d)\.(\d)$",ip)
    li=[]
    for i in range(1,4):
        li.append(int(ipv4.group(i)))
    for i in range(len(li)):
        if li[i]>255:
            return False
    return True


if __name__ == "__main__":
    main()




