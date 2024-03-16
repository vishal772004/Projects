def  main():
    first=input("Fraction:")
    percentage=convert(first)
    final=gauge(percentage)
    print(final)

def convert(first):
    while True:
        try:
            x,y=first.split("/")
            x=int(x)
            y=int(y)
            if y==0:
                raise ZeroDivisionError
            if x>y:
                raise ValueError
            per=(x/y)
            if per<=1:
                return int(per*100)
            else:
                first=input("Fraction:")
        except (ValueError,ZeroDivisionError):
            raise


def gauge(p):
    if p<=1:
        return "E"
    elif p>=99:
        return "F"
    elif (p-int(p)>=0.5):
        return str(int(p+1))+"%"
    else:
        return str(p)+"%"

if __name__=="__main__":
    main()

