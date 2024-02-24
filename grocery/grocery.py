l=[]
while True:
    try :
        g=input().upper()
        l.append(g)
    except EOFError:
        break
z=1
d={}
k=[]
a=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for  i in l:
    for j in l:
        if i==j:
            z=z+1
            l.remove(j)
        d[i]=z
        z=1
for i in a:
    for j in l:
        if j.startswith(i):
            print(z,j)


