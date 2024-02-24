l=[]
while True:
    try :
        g=input().upper()
        l.append(g)
    except EOFError:
        break
z=0
d={}
s=set()
a=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
x=len(l)
for k in l:
    for m in l:
        if k==m:
            z=z+1
            print(z)
            print(l)
        if z>=2:
            l.remove(m)
            print("5")
            print(l)
            print(z)
    d[k]=z
    z=0

for i in a:
    for j in l:
        if j.startswith(i):
            print(d[j],j)





