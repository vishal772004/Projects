print("Amount Due:50")
do:
    amt=int(input("Insert coin:"))
    if amt==5 or amt==10 or amt==25:
        amt=50-amt
        print("Change owed:",amt)
while amt!=0:
