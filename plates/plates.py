def main():

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    l=[]
    for i in plate:
        l.append(i)
        if i.isdigit():
            

    if plate[0].isalpha() or plate[1].isalpha():
        pass
    else:
        return False
    if 2>len(l)<=6:
        pass
    else:
        return False
    if plate.isalnum():
        pass
    else:
        return False



plate= input("Plate: ")

main()
