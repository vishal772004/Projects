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
    if 2<=len(l)<=6:
        pass
    else:
        return False
    c=l[0]
    c1=l[1]
    if c.isalpha() and c1.isalpha():
        pass
    else :
        return False

    return True


main()
