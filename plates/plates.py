def main():

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    l=[]
    j=0
    for i in plate:
        l.append(i)
        if i.isdigit():
            if i==0 and j==0:
                return True
            j=j+1
    if plate[-1].isdigit():
        pass
    else:
        return


    if plate[0].isalpha() or plate[1].isalpha():
        pass
    else:
        return
    if 2>len(l)<=6:
        pass
    else:
        return
    if plate.isalnum():
        pass
    else:
        return



plate= input("Plate: ")

main()
