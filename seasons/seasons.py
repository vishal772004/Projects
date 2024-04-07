import datetime

def main():
    _date=Datetime.get()
    print(_date)

class Datetime():
    def __init__(self,date,month,year):
        self.date=int(date)
        self.month=int(month)
        self.year=int(year)

    def __str__(self):
        start_date = datetime.date(self.year , self.month , self.date)
        return str(start_date)

    @classmethod
    def get(cls):
        year,month,date =input("Date of Birth:").split("-")
        return cls(date,month,year)


if __name__ == "__main__":
    main()
