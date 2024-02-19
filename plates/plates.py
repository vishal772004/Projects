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
    if s.isalnum():
        


    print(l)
    return True


main()
