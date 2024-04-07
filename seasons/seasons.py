import datetime,sys,inflect

def main():
    p = inflect.engine()
    try:
        _date=Datetime.get()
    except ValueError:
        sys.exit("Invalid Date")
    date_=Datetime.gettoday()
    final = _date-date_
    final = final*60
    words = p.number_to_words(final,andword=", ")
    print(words)

class Datetime():
    def __init__(self,date,month,year):
        self.date=int(date)
        self.month=int(month)
        self.year=int(year)

    def convert(self):
        ...

    def __sub__(self,other):
        date = self.date-other.date
        month = self.month-other.month
        year = self.year-other.year
        return Datetime(date,month,year)

    @classmethod
    def gettoday(cls):
        year,month,date=datetime.date.today().split(",")
        return cls(year,month,date)
    @classmethod
    def get(cls):
        year,month,date =input("Date of Birth:").split("-")
        return cls(date,month,year)


if __name__ == "__main__":
    main()
