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
    if 2<=len(l)<=6:
        pass
    else:
        return False
    if j>0 and l[-1]>0 and l[-1]<9 :
        pass
    else :
        return False
    if s.isalnum():
        pass
    else :
        return False


    print(l)
    return True


main()
