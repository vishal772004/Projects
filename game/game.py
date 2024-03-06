
while True:
    try:
        level=int(input("Level:"))
        break
    except ValueError:
        continue
print(level)
