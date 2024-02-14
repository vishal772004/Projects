print("Amount Due:50")
amt=int(input("Insert Coin:"))
amt1=50
while amt1>=amt:
    if amt==5 or amt==10 or amt==25:
        amt=amt1-amt
        if amt>0:
            print("Amount Due:",amt)
    elif amt1==50:
        print("Amount Due:50")
    amt1=amt
    if amt1!=0:
        amt=int(input("Insert Coin:"))
    else:
        break

print("Change Owed:",amt1)



