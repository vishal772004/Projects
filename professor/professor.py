import random

def main():
    level1=get_level()
    score=generate_integer(level1)
    print("Score:",score)

def get_level():
    while True:
        n=int(input("Level:"))
        if n<=0 and n>3:
            continue
        break
    return n

def generate_integer(level):
    n=1
    score=10
    while n<=10:
        first=random.randint(0,level*10)
        second=random.randint(0,level*10)
        answer=first+second
        try:
            print(f"{first}+{second}=",end=" ")
            l=int(input())
            for i in range(2):
                if l==answer:
                    break
                else:
                    print("EEE")
                    print(f"{first}+{second}=",end=" ")
                    l=int(input())
                    score=score-1
            n=n+1
        except ValueError:
            continue

    return score

if __name__ == "__main__":
    main()
