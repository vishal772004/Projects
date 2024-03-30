
import validators
def main():
    mail=input("What's your email address?")
    print(validate(mail))

def validate(s):
   # if re.search("^[a-zA-Z0-9]*@[a-zA-Z0-9]*\.com$",s,re.IGNORECASE):
    if validators.email("someone@example.com")
        return "Valid"
    else:
        return "Invalid"

if __name__=="__main__":
    main()
