list_of_name=[]

while True:
    print("Name:")
    try:

        name=input()
        list_of_name.append(name)
    except EOFError:
        print("Adieu, adieu, to",end=" ")
        break

for i in list_of_name:
    if list_of_name[0]==i and len(list_of_name)==1:
        print(i)
        break
    elif list_of_name[-1]==i:
        print("and",i)
    else:
        print(i,end=", ")



