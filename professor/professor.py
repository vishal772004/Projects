import random


def main():
    level1=get_level()
    print(level1)



def get_level():
    while True:
        n=int(input("Level:"))
        if n<=0 and n>3:
            continue
        break
    return n


def generate_integer(level):
    n=1
    while n<=10:
        first=random.randint(0,level*10)
        second=random.randint(0,level*10)
        answer=first+second
        l=int(input(first"+"+second+"="))
        for i in range(2):
            




if __name__ == "__main__":
    main()
