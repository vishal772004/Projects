import sys
import csv
def main():
    if len(sys.argv)<3:
        sys.exit("Too few command line arguments")
    elif len(sys.argv)>3:
        sys.exit("Too many command line arguments")
    else:
        if not(sys.argv[1].endswith(".csv")):
            sys.exit("Could not read",sys.argv[1])
        hogwarts=[]
        with open(sys.argv[1]) as file:
            read=csv.DictReader(file)
            for i in read:
                hogwarts.append(i)
        with open(sys.argv[2],"a") as file1:
            writer = csv.DictWriter(file1, fieldnames=['name','house'])
            writer.writeheader()
            #writer.writerows(hogwarts)
            for i in hogwarts:
                print(i['name'])
if __name__=="__main__":
    main()

