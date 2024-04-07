import datetime

def main():
    _date=Datetime.get()

class Datetime():
    def __init__(self,date,month,year):
        self.date=int(date)
        self.month=int(month)
        self.year=int(year)

    def check(self):
        start_date = datetime.date(self.year , self.month , self.date)
        print(start_date)

    @classmethod
    def get(cls):
        year,month,date =input("Date of Birth:")
        return cls(date,month,year)


if __name__ == "__main__":
    main()
