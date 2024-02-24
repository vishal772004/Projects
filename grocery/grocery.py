l=[]
while True:
    try :
        g=input().upper()
        l.append(g)
    except EOFError:
        break
z=0
print(l)
d={}
a=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for i in l:
    for j in l:
        if i==j:
            z=z+1
    for k in i:
        for l in a:
            if k==a:
                d[i]=len(a)
print(d)


