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
        with open(sys.argv[1]) as file:
            read=csv.DictReader(file)
        print(read)

if __name__=="__main__":
    main()

