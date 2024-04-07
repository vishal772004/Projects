import datetime,sys,inflect

def main():
    p = inflect.engine()
    try:
        _date=Datetime.get()
    except ValueError:
        sys.exit("Invalid Date")
    words = p.number_to_words(_date)
    print(words)

class Datetime():
    def __init__(self,date,month,year):
        self.date=int(date)
        self.month=int(month)
        self.year=int(year)

    def convert(self):
        start_date = datetime.date(self.year , self.month , self.date)
        


    @classmethod
    def get(cls):
        year,month,date =input("Date of Birth:").split("-")
        return cls(date,month,year)


if __name__ == "__main__":
    main()
