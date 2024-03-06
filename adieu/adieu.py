list_of_name=[]
output=""
while True:
    try:
        name=input()
        list_of_name.append(name)
    except EOFError:
        print("Adieu, adieu, to",end=" ")
        break
for i in list_of_name:
    if len(list_of_name)==1:
        print(i,end=" ")
    if list_of_name[-1]==i:
        print("and",i,)
    else:
        print(i,sep=",",end=" ")




