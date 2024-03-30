import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
  #  try:
        if time:=re.search("^([1-9]|[1][0-2])?(:[0-5][0-9])? (AM|PM)+ to ([1-9]|[1][0-2])?(:[0-5][0-9])? (AM|PM)+$",s):
            li=s.split(" to ")
            for i in range(len(li)):
                if li[i].find(":")<=0:
                    hour,minute=li[i].split(":")
                else:
                    hour=li[i]


if __name__ == "__main__":
    main()
