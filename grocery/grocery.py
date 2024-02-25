l=y=[]
while True:
    try :
        g=input().upper()
        l.append(g)
    except EOFError:
        break
z=0
d={}

a=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
s=set()
for k in l:
    z=0
    for m in l:
        if k==m:
            z=z+1
            d[k]=z
for i in l:
    try:
        s.add(i)
    exception 
for i in a:
    for j in l:
        if j.startswith(i):
            print(d[j],end=" ")
            print(j)





