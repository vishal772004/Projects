import csv

def main():
    print("\tWelcome to Movie Mania \t")
    print("On what basis do you want to find your movie :")
    print("1.Rating\n2.Movie Name\n3.Genre\n4.Movieyear\n5.Star Cast\n6.Language\n7.Random Movie")
    choice=int(input("Please Enter your choice:"))
    match choice:
        case 1: Rating()

def Rating():
    row = csv_Reader()
    rating = [ r['rating'] for r in row ]
    for i in rating:
        print("Top )
    print(rating)

def function_2():
    ...


def function_n():
    ...
def csv_Reader():
    row=[]
    with open("IMDBTop250.csv") as file:
        reader = csv.DictReader(file)
        for rows in reader:
            row.append(rows)
    return row

if __name__ == "__main__":
    main()
