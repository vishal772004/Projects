import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ipv4=re.search(r"^([0-2]?[0-9][0-9])+\.([0-2]?[0-9][0-9])+\.([0-2]?[0-9][0-9])+\.([0-2]?[0-9][0-9])+$",ip)
    li=[]
    print(ipv4.group(1))
    for i in range(len(li)):
        if li[i]>255:
            return False
    return True


if __name__ == "__main__":
    main()




