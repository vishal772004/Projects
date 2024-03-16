def  main():
    while True:
        try:
            first=input("Fraction:")
            convert(first)

            break
        except ValueError:
            continue
        except ZeroDivisionError:
            continue
def convert(first):
    if first.find(".")>=0:
        continue
    else:
        pass
    l=first.split("/")
    x=int(l[0])
    y=int(l[-1])
    if x>y:
        continue
    return (x/y)*100

if p<=1:
    print("E")
elif p>=99:
    print("F")
elif (p-int(p)>=0.5):
    print(int(p+1),"%",sep="")
else:
     print(int(p),"%",sep="")



