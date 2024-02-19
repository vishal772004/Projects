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
    for i in l:
        if i.isdigit():
            j=j+1
    a=len(l)
    if j>0 and l[-1].isdigit():
        pass
    else:
        return False
    if s.isalnum():
        pass
    else:
        return False
    print(l)
    return True


main()
