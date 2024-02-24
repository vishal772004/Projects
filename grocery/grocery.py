l=[]
while True:
    try :
        g=input().upper()
        l.append(g)
    except EOFError:
        break
z=0
for i in l:
    for j in l:
        if i==j:
            z=z+1
        

