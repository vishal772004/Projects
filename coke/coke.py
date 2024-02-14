print("Amount Due:50")
amt=int(input("Insert coin:"))
amt1=50-amt
while amt!=0:
     if amt==5 or amt==10 or amt==25:
         amt1=50-amt
         print("Change owed:",amt)
     amt=int(input("Insert coin:"))
