print("Amount Due:50")
amt=int(input("Insert coin:"))
amt1=50
while amt!=0:
     if amt==5 or amt==10 or amt==25:
         if amt1>amt:
            amt=amt1-amt
            if amt>0:
                print("Amount Due:",amt)
            else:
                print("Amount Due:50")
     amt1=amt
     if amt>amt1:
         print("Change Owed:",amt1)
     elif amt1==0:
         print("Change Owed:",amt1)
     if amt1>=0:
         amt=int(input("Insert coin:"))
