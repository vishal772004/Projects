import random
import sys
while True:
    level=int(input("Level:"))
    try:

        guess=int(input("Guess:"))
        if guess<1 or guess>100 :
            continue
        if guess>level:
            print("Too large!")
            sys.exit(1)
        number=random.randint(1,level)
        if guess<number:
            print("Too small!")
        elif guess>number:
            print("Too large!")
        elif guess==number:
            print("Just right!")
            break
        else:
            continue
    except ValueError:
        continue

