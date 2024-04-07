import datetime,sys,inflect

def main():
    p = inflect.engine()
    try:
        _date=Datetime.get()
    except ValueError:
        sys.exit("Invalid Date")
    date_=Datetime.gettoday()
    final = date_-_date
    seconds = datetime.timedelta().total_seconds()
    seconds = seconds*60
    words = p.number_to_words(seconds,andword=", ")
    print(final,"minutes")

class Datetime():
    def __init__(self,date,month,year):
        self.date=int(date)
        self.month=int(month)
        self.year=int(year)
    def __str__(self):
        return f"{self.year}-{self.month}-{self.date}"

    def __sub__(self,other):
        date = self.date-other.date
        month = self.month-other.month
        year = self.year-other.year
        return Datetime(date,month,year)

    @classmethod
    def gettoday(cls):
        year,month,date=str(datetime.date.today()).split("-")
        return cls(year,month,date)
    @classmethod
    def get(cls):
        year,month,date =input("Date of Birth:").split("-")
        return cls(date,month,year)


if __name__ == "__main__":
    main()
