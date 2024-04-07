from datetime import date


def main():
    try:
        year,month,date = input("Date of Birth:").split("-")
    except ValueError:
        print("Invalid date")

    Date=Datetime(date,month,year)
    start_date = datetime.date(2015, 5, 1)
    print(start_date)



class Datetime():
    def __init__(self,date,month,year):
        self.date=date
        self.month=month
        self.year=year
        print(f"{self.date} is  the date and {self.month} is the month and {self.year} is the year")

if __name__ == "__main__":
    main()
