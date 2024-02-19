def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    l=[]
    for i in s:
        l.append(i)
        if i>0 && i<9:
            


    print(l)
    return True


main()
