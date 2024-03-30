import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
        if re.search("^([1-9]|[1][0-2])?(:[0-5][0-9])? (AM|PM)+ to ([1-9]|[1][0-2])?(:[0-5][0-9])? (AM|PM)+$",s):
            li=s.split(" to ")
            for i in range(len(li)):
                time,meridian=li[i].split(" ")
                if time.find(":")>0:
                    hour,minute=time.split(":")
                else:
                    hour=time
                if meridian=="PM":
                     r=int(hour)+12
                     if hour!="12":
                        li[i]=li[i].replace(hour,str(r))
                     li[i]=li[i].replace("PM","")
                li[i]=li[i].replace("AM","")
                if time.find(":")<=0:
                    li[i]=li[i].strip()+":00 "

            return li[0]+"to "+li[1].strip()
        raise ValueError

if __name__ == "__main__":
    main()
