import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if time:=re.search("^[0-9]+(:[0-9]+) (AM|PM)+ to [0-9]+(:[0-9]+) (AM|PM)+$",s):
        li=s.split(" to ")
        for i in li:
            if i.find("PM")>0:
                r=int(li[i][0])+12
                li[i]=li[i].replace("PM","")
                li[i]=li[i].replace(li[i][0],str(r))
            li[i]=li[i].replace("AM","")
            



if __name__ == "__main__":
    main()
