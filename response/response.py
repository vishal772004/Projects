import re

def main():
    mail=input("What's your email address?")
    print(validate(mail))

def validate(s):
    if re.search("^[a-zA-Z0-9_]*@[a-zA-Z0-9]\.com$",s,re.IGNORECASE):
        return "Valid"
    else:
        return "Invalid"

if __name__=="__main__":
    main()
