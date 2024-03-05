list_of_name=[]
i=0
while True:
    try:
        name=input("Name:")
        list_of_name[i]=name
        i=i+1
    except EOFError:
        break
print("Adieu,adieu,to ")
for i in list_of_name:
    if list_of_name[-1]==i:
        print("and ",list_of_name[-1])
    print(i,end=",")



