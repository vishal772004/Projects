list_of_name=[]

while True:
    try:
        name=input("Name:")
        list_of_name.append(name)
    except EOFError:
        print("\n")
        break
print("Adieu, adieu, to",end=" ")
for i in list_of_name:
    if list_of_name[0]==i and len(list_of_name)<=1:
        print(i)
        break
    elif list_of_name[-1]==i:
        print("and",i)
    else:
        print(i,end=", ")



