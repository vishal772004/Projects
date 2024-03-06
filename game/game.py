import random
import sys
while True:
    try:
        level=int(input("Level:"))
        guess=int(input("Guess:"))
        if guess<1 or guess>100 :
            continue
        if guess>level:
            print("Too large!")
        break
    except ValueError:
        continue
number=random.randint(1,level)
if guess<number:
    print("Too small!")
elif guess>number:
    print("Too large!")
elif guess==number:
    print("Just right!")
