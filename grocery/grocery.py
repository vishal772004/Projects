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
    z=0
    for m in l:
        if k==m:
            z=z+1

        if z>=2:
            l.remove(m)

    d[k]=z
    print(d)


for i in a:
    for j in l:
        if j.startswith(i):
            print(d[j],end=" ")
            




