import csv
import sys
import re
def main():
    print("\tWelcome to Movie Mania \t")
    print("On what basis do you want to find your movie :")
    print("1.Rating\n2.Genre\n3.Movieyear\n4.Star Cast\n5.Language\n6.Random Movie")
    choice=int(input("Please Enter your choice:"))
    match choice:
        case 1: Rating()
        case 2: genre()
        case 3: year()
        case 4: cast()
        case _: print("Invalid Choice")

def Rating():
    row = csv_Reader()
    rating = [ r['rating'] for r in row ]
    movieName = [m['movieTitle'] for m in row]
    print("Top 10 movies are:")
    j=0
    n=10
    count=0
    print("Ranking\tRating\t Movie Name")
    while j!=250:
        while j<=n:
            if j>=250:
                if count==0:
                    sys.exit("No Movies Found")
                sys.exit("The End")
            print(j+1,"\t",rating[j],"\t",movieName[j])
            count=1
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
    print("What kind of movies do you like:")
    print("1.Action\n2.Adventure\n3.Drama\n4.Crime\n5.History\n6.Comedy\n7.Fantasy\n8.Animation")
    option=int(input("Enter your choice:"))
    match option:
        case 1: genres(1)
        case 2: genres(2)
        case 3: genres(3)
        case 4: genres(4)
        case 5: genres(5)
        case 6: genres(6)
        case 7: genres(7)
        case 8: genres(8)
        case _: sys.exit("Inavlid option")

def genres(s):
    row = csv_Reader()
    movieName = [m['movieTitle'] for m in row]
    Genre = [g['genre'] for g in row]
    j=0
    n=10
    i=1
    count=0
    print("Ranking")
    while j!=250:
        while i<=n:
            if j>=250:
                if count==0:
                    sys.exit("No Movies Found")
                sys.exit("The End")
            if option1(s,Genre[j]):
                print(j+1,"\tGenre=",Genre[j])
                print("\t\tMovie name=",movieName[j])
                count=1
                i+=1
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

def option1(s,Gen):
    match s:
        case 1:
            if re.search(".*(Action).*",Gen):
                return True
        case 2:
            if re.search(".*(Adventure).*",Gen):
                return True
        case 3:
            if re.search(".*(Drama).*",Gen):
                return True
        case 4:
            if re.search(".*(Crime).*",Gen):
                return True
        case 5:
            if re.search(".*(History).*",Gen):
                return True
        case 6:
            if re.search(".*(Comedy).*",Gen):
                return True
        case 7:
            if re.search(".*(Fantasy).*",Gen):
                return True
        case 8:
            if re.search(".*(Animation).*",Gen):
                return True

def year():
    row = csv_Reader()
    movieYear = [m['movieYear'] for m in row]
    movieName = [m['movieTitle'] for m in row]
    year_of_release = int(input("Enter the Year of Release to search  for a Movie:"))
    n=10
    j=0
    count=0
    i=1
    while j!=250:
        while i<=n:
            if j>=250:
                if count==0:
                    sys.exit("No Movies Found")
                sys.exit("The End")
            if year_of_release==int(movieYear[j]):
                if i==1:
                     print("Ranking\t Year\t Movie")
                print(j+1,"\t",movieYear[j],"\t",movieName[j])
                i+=1
                count=1
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

def cast():
    row = csv_Reader()
    movieName = [m['movieTitle'] for m in row]
    starList = [m['starList'].lower() for m in row]
    star = input("Enter any cast member of a movie:").lower().strip()
    n=10
    j=0
    count=0
    i=1
    while j!=250:
        while i<=n:
            if j>=250:
                if count==0:
                    sys.exit("No Movies Found")
                sys.exit("The End")
            if star in starList[j]:
                print(movieName[j])
                i+=1
                count=1
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
