import datetime,sys,inflect

def main():
    try:
        birth_date=input("Date of Birth:")
    except ValueError:
        sys.exit("Invalid Date")

class Birthdate:
    def __init__(self,birth_date):
        self.year,self.month,self.date=birth_date.split("-")




if __name__ =="__main__":
    main()
