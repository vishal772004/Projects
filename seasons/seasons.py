import datetime,sys,inflect,re

def main():
    try:
        birth_date=input("Date of Birth:")
        if re.search("^[0-9][0-9][0-9][0-9]-([0][0-9]||[1][0-2])+-([0][0-9]||[0-3][0-9])+$",birth_date):
            pass
        else:
            raise ValueError
    except ValueError:
        sys.exit("Invalid Date")

    
class Birthdate:
    def __init__(self,birth_date):
        self.year,self.month,self.date=birth_date.split("-")




if __name__ =="__main__":
    main()
