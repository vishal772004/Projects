import re
num = input("Number:")
prod = 1
sum = 0
l = []
for i in num:
    l.append(int(i))
for i in range(len(l)):
    if i%2==0 or i==0:
        prod = prod + (l[i]*2)
    else:
        sum = sum + l[i]
if((prod+sum)%10==0):
    pass
else:
    print("INVALID")

if()
