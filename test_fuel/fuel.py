def main():
    while True:
        try:
            first=input("Fraction:")
            p=convert(first)
            print(gauge(p),end="")
            if gauge(p)
            break
        except ValueError:
            continue
        except ZeroDivisionError:
            continue
def gauge(p):
    if p<=1:
        return("E")
    elif p>=99:
        return("F")
    elif (p-int(p)>=0.5):
        return int(p+1)
    else:
        return int(p)

def convert(fraction):
    if fraction.find(".")>=0:
        continue
    else:
        pass
    l=first.split("/")
    x=int(l[0])
    y=int(l[-1])
    if x>y:
        continue
    return (x/y)*100

if __name__ == "__main__":
    main()


