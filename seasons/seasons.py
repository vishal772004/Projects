import datetime,sys,inflect,re

def main():
    birth_date=input("Date of Birth:")
    p=inflect.engine()
    date_of_birth=check(birth_date)
    date_=datetime.date(int(year),int(month),int(date))
    today=datetime.date.today()
    final=convert(date_of_birth,today)
    total_minutes=final.days
    words=p.number_to_words(total_minutes,andword=", ").lstrip("minus ")
    print(words,"minutes")

def check(birth_date):
    try:
        if re.search("^[0-9][0-9][0-9][0-9]-([0][0-9]||[1][0-2])+-([0][0-9]||[0-3][0-9])+$",birth_date):
            pass
        else:
            raise ValueError
    except ValueError:
        sys.exit("Invalid Date")
    year,month,date=birth_date.split("-")
    return (year,month,date)
def convert(date_of_birth,today):
    final=today-date_of_birth
    total_minutes=-(final*24*60)
    return total_minutes


if __name__ =="__main__":
    main()
