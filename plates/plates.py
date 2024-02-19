def main():
    plate= input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    l=[]
    j=0
    for i in s:
        l.append(i)
        if i.isdigit():
            if i==0 and j==0:
                return True
            j=j+1
        if s[-1].isdigit():
             pass
        else:
             return False


    if s[0].isalpha() or s[1].isalpha():
        pass
    else:
        return False
    if 2>len(l)<=6:
        pass
    else:
        return False
    if s.isalnum():
        pass
    else:
        return False
    return True
main()
