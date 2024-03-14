def main():
    while True:
        try:
            first=input("Fraction:")
            if first.find(".")>=0:
                continue
            else:
                pass
            p=convert(first)
            print(gauge(p),end="")
            if 0<gauge(p)<100:
                print("%")
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
    l=fraction.split("/")
    x=int(l[0])
    y=int(l[-1])
    return (x/y)*100

if __name__ == "__main__":
    main()


