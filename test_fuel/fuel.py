def main():
    while True:
        try:
            first=input("Fraction:")
            if first.find(".")>=0:
                continue
            else:
                pass

            p=convert(first)
            gauge(p)
            break
        except ValueError:
            continue
        except ZeroDivisionError:
            continue
def gauge(p):
    if p<=1:
        print("E")
    elif p>=99:
        print("F")
    elif (p-int(p)>=0.5):
        print(int(p+1),"%",sep="")
    else:
        print(int(p),"%",sep="")

def convert(first):
    l=[]
    l=first.split("/")
    x=int(l[0])
    y=int(l[-1])
    if x>y:
        continue
    p=(x/y)*100
    return p

if __name__=="__main__":
    main()
