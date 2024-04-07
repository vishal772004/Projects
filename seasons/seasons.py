import datetime,sys,inflect

def main():
    p = inflect.engine()
    try:
        _date=Datetime.get()
    except ValueError:
        sys.exit("Invalid Date")
    date_=Datetime.today()
    words = p.number_to_words(_date,andword=", ")
    print(words)

class Datetime():
    def __init__(self,date,month,year):
        self.date=int(date)
        self.month=int(month)
        self.year=int(year)

    def today(self):
        start_date = datetime.date.today()
        end_date = datetime.date(self.year , self.month , self.date)

    def __sub__(self,other):
        date = self.date-other.date
        month = self.month-other.month
        year = self.year-other.year
        return Datetime(date,month,year)




    @classmethod
    def get(cls):
        year,month,date =input("Date of Birth:").split("-")
        return cls(date,month,year)


if __name__ == "__main__":
    main()
