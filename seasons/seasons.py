import datetime,sys,inflect,re

def main():
    try:
        birth_date=input("Date of Birth:")
        if re.search("^[0-9][0-9][0-9][0-9]-([0][0-9]||[1][0-2])+-([0][0-9]||[0-3][0-9])+$",birth_date):
            pass
        else:
            raise ValueError
    except ValueError:
        sys.exit("Invalid Date")

    dob=Birthdate(birth_date)
    date_of_birth=dob.check(birth_date)
    print(date_of_birth)
class Birthdate:
    def __init__(self,birth_date):
        self.year,self.month,self.date=birth_date.split("-")
    def check(self,birth_date):
        self.year=int(year)
        self.month=int(month)
        self.date=int(date)
        date_=datetime.date(birth_date)
        return date_

if __name__ =="__main__":
    main()
