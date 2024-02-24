l=[]
while True:
    try :
        g=input().upper()
        l.append(g)
    except EOFError:
        break
for i in l:
    for j in l:
        if l[i]<l[j]:
            print(l[i])
