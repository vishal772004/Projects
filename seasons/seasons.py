import datetime

def main():
    try:
        year,month,date = input("Date of Birth:").split("-")
    except ValueError:
        print("Invalid date")

class Datetime():
    def __init__(self,date,month,year):
        self.date=date
        self.month=month
        self.year=year

    def check(self):
        Date = datetime.date(date,month,year)
if __name__ == "__main__":
    main()
