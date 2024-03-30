import re

def main():
    mail=input("What's your email address?")
    print(validate(mail))

def validate(s):
    if re.search("^[a-zA-Z0-9]*@",s,re.IGNORECASE):
        return "Valid"
    else:
        return "Invalid"

if __name__=="__main__":
    main()
