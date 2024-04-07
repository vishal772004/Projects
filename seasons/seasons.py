from datetime import date


def main():
    try:
        year,month,date = input("Date of Birth:").split("-")

    except ValueError:
        print("Invalid date")

    date=Datetime(date,month,year)
    date.MINYEAR("1900")
    date.calender()

class Datetime():
    def __init__(self,date,month,year):
        self.date = date
        self.month = month
        self.year = year

    def calender(self):
        return f"Date :{self.date}-Month :{self.month}-Year :{self.year}"


if __name__ == "__main__":
    main()
