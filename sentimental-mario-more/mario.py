import sys

height = int(input("Height:"))
if(height<=0)
    sys.exit(1)

for i in range(height):
    for k in range(height-i):
        print(" ",end="")
    for l in range(i+1):
        print("#",end="")
    print("  ",end="")
    for j in range(i+1):
        print("#",end="")
    print()
