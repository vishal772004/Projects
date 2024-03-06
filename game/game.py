import random
while True:
    try:
        level=int(input("Level:"))
        guess=int(input("Guess:"))
        break
    except ValueError:
        continue
number=random.randint(1,100)
if level<number:
    print("Too small!")
elif number>level:
    print("Too large!")
else:
    print("Just right!")
