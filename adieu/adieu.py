list_of_name=[]

while True:
    try:
        name=input("Name:")
        i=0
        list_of_name[i]=name
        i=i+1
    except EOFError:
        break
print("Adieu,adieu,to ")
for i in list_of_name:
    if list_of_name[-1]==i:
        print("and ",list_of_name[-1])
    print(i,end=",")



