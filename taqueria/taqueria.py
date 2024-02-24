menu={
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}
sum=0
print("Item:")
while True:
    try:
        item=input().lower()
        if item in menu:
            sum=sum+menu[item]
        continue
    except EOFError:
        print("\n")
        break
    except KeyError:
        continue
print(f"${sum:.2f}")
