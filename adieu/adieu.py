list_of_name=[]

while True:
    try:
        name=input("Name:")
        list_of_name.append(name)
    except EOFError:
        break
print("Adieu,adieu,to",end=" ")
for i in list_of_name:
    if list_of_name[-1]==i:
        print("and",list_of_name[-1])
    elif list_of_name[-2]==i:
        print(i,end=" ")



