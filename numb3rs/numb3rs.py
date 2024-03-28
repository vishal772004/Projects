import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ipv4=re.search(r"^(\d)\.(\d)\.(\d)\.(\d)$",ip)
    for i in range(1,3):
        if 0<int(ipv4.group(i))<=255:
            return False
    return True


if __name__ == "__main__":
    main()




