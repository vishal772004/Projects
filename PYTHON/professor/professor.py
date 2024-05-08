import random
import math
def main():
    level1=get_level()
    score=generate_integer(level1)
    print("Score:",score)

def get_level():
    while True:
        try:
            n=int(input("Level:"))
            if n==1 or n==2 or n==3:
                return n
            else:
                continue
        except ValueError:
            continue

def generate_integer(level):
    n=1
    score=10
    while n<=10:
        first=generate_number(level)
        second=generate_number(level)
        answer=first+second
        try:
            print(f"{first} + {second} =",end=" ")
            l=int(input())
            for i in range(2):
                if l==answer:
                    break
                else:
                    print("EEE")
                    print(f"{first} + {second} =",end=" ")
                    l=int(input())
            if l!=answer:
                print(f"{first} + {second} =",answer)
                score=score-1
            n=n+1
        except ValueError:
            print("EEE")
            continue

    return score

def generate_number(level):
    if level==1:
        x=random.randint(math.pow(10,(level-1))-1,math.pow(10,level)-1)
    else:
        x=random.randint(math.pow(10,(level-1)),math.pow(10,level)-1)
    return x

if __name__ == "__main__":
    main()
