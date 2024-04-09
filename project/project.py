import csv

def main():
    print("\tWelcome to Movie Mania \t")
    print("On what basis do you want to find your movie :")
    print("1.Rating\n2.Genre\n3.Movieyear\n4.Star Cast\n5.Language\n6.Random Movie")
    choice=int(input("Please Enter your choice:"))
    csv_Reader()
def Rating():
    ...


def function_2():
    ...


def function_n():
    ...
def csv_Reader():
    with open("IMDBTop250.csv") as file:
        reader = csv.DictReader(file)
        rating = {row for row in reader if rating>9}
        print(rating)



if __name__ == "__main__":
    main()
