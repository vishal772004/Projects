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
    p=inflect.engine()
    dob=Birthdate(birth_date)
    date_of_birth=dob.check(birth_date)
    today=datetime.date.today()
    total_minutes=convert(date_of_birth,today)
    words=p.number_to_words(total_minutes,andword=", ").lstrip("minus ")
    print(words,"minutes")
class Birthdate:
    def __init__(self,birth_date):
        self.year,self.month,self.date=birth_date.split("-")
    def check(self,birth_date):
        date_=datetime.date(int(self.year),int(self.month),int(self.date))
        return date_
def convert(date_of_birth,today):
    print(type(today))
    final=today-date_of_birth
    total_minutes=-(final*24*60)
    return total_minutes


if __name__ =="__main__":
    main()
