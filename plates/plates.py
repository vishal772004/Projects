def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    l=[]
    j=0
    for i in s:
        l.append(i)
        if i>=0 and i<=9:
            j=j+1



    print(l)
    return True


main()
