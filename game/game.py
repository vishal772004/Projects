import random
import sys
while True:
    try:
        level=int(input("Level:"))
        guess=int(input("Guess:"))
        if guess<1 or guess>100 :
            continue
        if guess>level:
            sys.exit()
        break
    except ValueError:
        continue
number=random.randint(1,level)
if guess<number:
    sys.exit()
elif guess>level:
    print("Too large!")
else:
    print("Just right!")
