import re
import sys
def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    try:
        ipv4=re.search(r"^(\d*\d*\d*)\.(\d*\d*\d*)\.(\d*\d*\d*)\.(\d*\d*\d*)$",ip)
        li=[]
        for i in range(1,5):
            v=ipv4.group(i)
            li.append(int(v))
        if li[0]>255:
            return False
        return True
    except AttributeError:
        return False

if __name__ == "__main__":
    main()




