def  main():
    fraction=input("Fraction:")
    percentage=convert(fraction)
    final=gauge(percentage)
    print(final)

def convert(fraction):
    while True:
        try:
            x,y=fraction.split("/")
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
                fraction=input("Fraction:")
                continue
        except (ValueError,ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage<=1:
        return "E"
    elif percentage>=99:
        return "F"
    elif (percentage-int(percentage)>=0.5):
        return str(int(percentage+1))+"%"
    else:
        return str(percentage)+"%"

if __name__=="__main__":
    main()

