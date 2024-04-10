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
    movieName = [m['movieTitle'] for m in row]
    ranking = [r['ranking'] for r in row]
    print("Top 10 movies are:")
    j=1
    n=10
    print("Ranking\tRating\t Movie Name")
    while j!=250:
        while j<=n:
            print(j,"\t",rating[j],"\t",movieName[j])
            j+=1
        option=input("Do you want the next top 10 movies: yes/no :")
        if option=="no" or option=="NO":
            break
        elif option=="yes" or option=="YES":
            n=n+10
            continue
        else:
            print("Invalid choice")
            continue


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
