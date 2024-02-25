l=[]
while True:
    try :
        g=input().upper()
        l.append(g)
    except EOFError:
        break
z=0
d={}

a=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

for k in l:
    for m in l:
        if k==m:
            print(k)

for i in a:
    for j in l:
        if j.startswith(i):
            print(j,end=" ")
           # print(j)





