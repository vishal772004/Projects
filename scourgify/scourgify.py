import sys
import csv
def main():
    if len(sys.argv)<3:
        sys.exit("Too few command line arguments")
    elif len(sys.argv)>3:
        sys.exit("Too many command line arguments")
    else:
        try:
            if not(sys.argv[1].endswith(".csv")):
                sys.exit("Could not read",sys.argv[1])
            before,after=[],[]
            with open(sys.argv[1]) as file:
                read=csv.DictReader(file)
                for i in read:
                    before.append(i)
            with open(sys.argv[2],"w") as file1:
                writer = csv.DictWriter(file1, fieldnames=['first','last','house'])
                for i in before:
                    str=i['name']
                    str=str.split(",")
                    after.append({'first':str[1],'last':str[0],'house':i['house']})
                writer.writerow({"first":"first","last":"last","house":"house"})
                writer.writerows(after)
        except FileNotFoundError:
            sys.exit("Could not find the csv file")
if __name__=="__main__":
    main()

