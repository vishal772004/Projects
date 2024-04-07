from datetime import date


def main():
    try:
        year,month,date = input("Date of Birth:").split("-")
    except ValueError:
        print("Invalid date")

    d=Datetime(date,month,year)
    d.__str__()
    print(f"Date :{self.date}-Month :{self.month}-Year :{self.year}")

class Datetime():
    def __init__(self,date,month,year):
        self.date = date
        self.month = month
        self.year = year

    def __str__(self):
        return f"Date :{self.date}-Month :{self.month}-Year :{self.year}"


if __name__ == "__main__":
    main()
