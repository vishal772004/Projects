import sys
import csv
import tabulate
def main():
    if len(sys.argv)<2:
        sys.exit("Too few command line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too many command line arguments")
    else:
        try:
            if not(sys.argv[1].endswith(".csv")):
                sys.exit("Not a CSV File")
            with open(sys.argv[1]) as file:
                read=csv.reader(file)
            for line in read:
                print(line)
        except FileNotFoundError:
            sys.exit("File does not exist")

if __name__=="__main__":
    main()
