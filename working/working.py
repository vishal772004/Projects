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
                    hour=li[i][2].strip()
                if li[i].find("PM")>0 :
                    r=int(hour)+12
                    li[i]=li[i].replace("PM","")
                    if hour!="12":
                        li[i]=li[i].replace(hour,str(r))
                li[i]=li[i].replace("AM","")
            for i in range(len(li)):
                if li[i].find(":")<=0:
                    li[i]=li[i]+":00"
            return li[0]+"to "+li[1].strip()
        raise ValueError
   # except ValueError:
     #   return None



if __name__ == "__main__":
    main()
