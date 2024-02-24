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
x=len(l)
for k in l:
    for m in l:
        

for i in a:
    for j in l:
        if j.startswith(i):
            print(j)


