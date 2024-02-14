amt=int(input("Amount Due:"))
while amt!=0:
    amt=int(input("Amount Due:"))
    if amt==5 or amt==10 or amt==25:
        amt=50-amt
        print("Change owed:",amt)
