import sys

while(True):
    height = input("Height:")
    if(height.isdigit() and int(height)>0):
        break
height = int(height)

for i in range(height):
    for k in range(height-i-1):
        print(" ",end="")
    for l in range(i+1):
        print("#",end="")
    print("  ",end="")
    for j in range(i+1):
        print("#",end="")
    print()
