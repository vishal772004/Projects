list_of_name=[]

while True:
    try:
        name=input("Name:")
        list_of_name.append(name)
    except EOFError:
        break
print("Adieu,adieu,to ")
for i in list_of_name:
    if list_of_name[-1]==i:
        print("and ",list_of_name[-1])
    print(i,end=",")



