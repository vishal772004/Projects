import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        if time:=re.search("^([0-1][0-9])?(:[0-5][0-9])? (AM|PM)+ to [0-9]+(:[0-5][0-9])? (AM|PM)+$",s):
            li=s.split(" to ")
            for i in range(len(li)):
                if li[i].find("PM")>0:
                    r=int(li[i][0])+12
                    li[i]=li[i].replace("PM","")
                    li[i]=li[i].replace(li[i][0],str(r))
                li[i]=li[i].replace("AM","")
            for i in range(len(li)):
                if li[i].find(":")<=0:
                    li[i]=li[i]+":00"

        return li[0]+"to "+li[1]
    except ValueError:
        return None



if __name__ == "__main__":
    main()
