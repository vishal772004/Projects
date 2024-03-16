def  main():
    while True:
        try:
            first=input("Fraction:")
            l=first.split("/")
            x=int(l[0])
            y=int(l[-1])
            if x>y:
                continue
            x=convert(x,y)
            print(gauge(x),end="")
            if 1<=float(gauge(x))<=100:
                print("%")
            break
        except ValueError:
            continue
        except ZeroDivisionError:
            continue
def convert(x,y):
    return float(x/y)*100

def gauge(p):
    if p<=1:
        return "E"
    elif p>=99:
        return "F"
    elif (p-int(p)>=0.5):
        return(int(p+1))
    else:
        return int(p)



