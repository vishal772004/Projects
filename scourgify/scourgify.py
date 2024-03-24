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
        hogwarts,after=[],[]
        with open(sys.argv[1]) as file:
            read=csv.DictReader(file)
            for i in read:
                hogwarts.append(i)
        with open(sys.argv[2],"a") as file1:
            writer = csv.DictWriter(file1, fieldnames=['name','house'])
            writer.writeheader()
            for i in hogwarts:
                str=i['name']
                str=str.split(",")
                full_name=str[1]+","+str[0]
                after.append({'name':full_name,'house':i})
            print(after)
            #writer.writerows(hogwarts)
if __name__=="__main__":
    main()

