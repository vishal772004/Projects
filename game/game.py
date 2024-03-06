import random
z=0
while True:
    try:
        if z==0:
            level=int(input("Level:"))
            z=z+1
        guess=int(input("Guess:"))
        if guess<1 or guess>100 :
            continue
        if guess>level:
            print("Too large!")
            continue
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

