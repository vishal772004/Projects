from datetime import date


def main():
    try:
        year,month,date = input("Date of Birth:").split("-")
    except ValueError:
        print("Invalid date")

    Date=Datetime(date,month,year)
    print(date.today())
    satrt_date=date(1999,05,02)



class Datetime():
    def __init__(self,date,month,year):
        self.date=date
        self.month=month
        self.year=year
        print(f"{self.date} is  the date and {self.month} is the month and {self.year} is the year")

if __name__ == "__main__":
    main()
