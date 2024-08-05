height = int(input("Height:"))
for i in range(height):
    for k in range(height-i):
        print(" ",end="")
    for l in range(i+1):
        print("#",end="")
    print("  ",end="")
    for j in range(i+1):
        print("#",end="")
    print()
