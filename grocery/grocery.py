l=[]
while True:
    try :
        g=input().upper()
        l.append(g)
    except EOFError:
        break
for i in l:
    for j in l:
        if i[0]<j[0]:
            print(l[i])
