print("Amount Due:50")
amt=int(input("Insert coin:"))
amt1=50
while amt>=0:

     if amt==5 or amt==10 or amt==25:
         if amt<amt1:
               amt=amt1-amt
               print("Amount Due:",amt)
         else:
               print("Amount Due:50")
     amt1=amt
     if amt


