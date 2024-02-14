print("Amount Due:50")
amt=int(input("Insert Coin:"))
amt1=50
while amt>0:
    if amt==5 or amt==10 or amt==25 and amt1>0:
        print("Amount Due:",amt1-amt)
    else:
        print("Amount Due:50")
    if amt1<amt:
        print("Change Owed:",amt1)
        break
    amt=int(input("Insert Coin:"))




