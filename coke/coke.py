print("Amount Due:50")
amt=int(input("Insert coin:"))
amt1=50
while amt>=0:

     if amt==5 or amt==10 or amt==25:
         if amt<=amt1:
               amt=amt1-amt
               if amt1>0 and amt!=0:
                    print("Amount Due:",amt)
               elif amt==50:
                    print("Amount Due:50")

     if amt==0 or amt>amt1:
          print("Change Owed :",amt)
          break
     if amt1>amt:
          amt=int(input("Insert coin:"))




