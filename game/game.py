import random
#import sys
while True:
    try:
        level=int(input("Level:"))
        guess=int(input("Guess:"))
        if guess<1 or guess>100 or guess>level:
            continue
        break
    except ValueError:
        continue
number=random.randint(1,level)
if guess<number:
    print("Too small!")
elif guess>level:
    print("Too large!")
else:
    print("Just right!")
