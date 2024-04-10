import csv
import sys

def main():
    print("\tWelcome to Movie Mania \t")
    print("On what basis do you want to find your movie :")
    print("1.Rating\n2.Genre\n3.Movieyear\n4.Star Cast\n5.Language\n6.Random Movie")
    choice=int(input("Please Enter your choice:"))
    match choice:
        case 1: Rating()
        case 2: genre()
        case _: print("Invalid Choice")

def Rating():
    row = csv_Reader()
    rating = [ r['rating'] for r in row ]
    movieName = [m['movieTitle'] for m in row]
    print("Top 10 movies are:")
    j=1
    n=10
    print("Ranking\tRating\t Movie Name")
    while j!=250:
        while j<=n:
            print(j,"\t",rating[j],"\t",movieName[j])
            j+=1
        option=input("Do you want the next 10 movies: yes/no :")
        if option=="no" or option=="NO":
            sys.exit("Enjoy your Movie")
        elif option=="yes" or option=="YES":
            n=n+10
            continue
        else:
            print("Invalid choice")
            continue


def genre():
    row = csv_Reader()
    movieName = [m['movieTitle'] for m in row]
    Genre = [g['genre'] for g in row]
    print("What kind of movies do you like:")
    option=int(input("1.Action\n2.Adventure\n3.Drama\n4.Crime\n5.History\n6.Comedy\n7.Fantasy\n8.Others"))
    match option:
        case 1:
            genres("Action")


def genres(s):
    while j!=250:
        while j<=n:
            print(j,"\t",rating[j],"\t",movieName[j])
            j+=1
        option=input("Do you want the next 10 movies: yes/no :")
        if option=="no" or option=="NO":
            sys.exit("Enjoy your Movie")
        elif option=="yes" or option=="YES":
            n=n+10
            continue
        else:
            print("Invalid choice")
            continue

def csv_Reader():
    row=[]
    with open("IMDBTop250.csv") as file:
        reader = csv.DictReader(file)
        for rows in reader:
            row.append(rows)
    return row

if __name__ == "__main__":
    main()
