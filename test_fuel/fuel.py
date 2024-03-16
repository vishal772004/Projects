def  main():
    first=input("Fraction:")
    percentage=convert(first)
    final=gauge(percentage)
    print(final)

def convert(x,y):
    while True:
        try:

            l=first.split("/")
            x=int(l[0])
            y=int(l[-1])
            if x>y:
                raise ValueError
            break
        except ValueError:
            raise
        except ZeroDivisionError:
            raise
    return int(x/y)*100

def gauge(p):
    if p<=1:
        return "E"
    elif p>=99:
        return "F"
    elif (p-int(p)>=0.5):
        return(int(p+1))+"%"
    else:
        return int(p)+"%"

if __name__=="__main__":
    main()

