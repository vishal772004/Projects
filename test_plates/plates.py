def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    l=[]
    j=0
    z=0
    for i in s:
        l.append(i)
        if i=="0" and j==0:
            return False
        if i.isdigit():
            j=j+1
            z=1
    if s.isalnum():
        pass
    else:
        return False
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
    if z==1:
        if l[-1].isdigit() and l[-2].isdigit():
            pass
        else:
            return False

    return True

if __name__ == "__main__":
    main()
