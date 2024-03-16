def  main():
    first=input("Fraction:")
    percentage=convert(first)
    final=gauge(percentage)
    print(final)

def convert(first):
    while True:
        try:
            l=first.split("/")
            x=int(l[0])
            y=int(l[-1])
            break
        except (ValueError,ZeroDivisionError):
            raise
    return (x/y)*100

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

