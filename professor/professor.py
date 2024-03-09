import random


def main():
    level1=get_level
    print(level1)



def get_level():
    while True:
        n=int(input("Level:"))
        if n<=0 and n>3:
            continue
        break
    return n


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()
