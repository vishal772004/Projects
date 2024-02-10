def main():
    time=input("What time is it?")



def convert(time):
    hours,minutes=int(time.split(":"))
    if hours==(7 or 8) and minutes<=60:
        print("breakfast time")
    elif hours==(12 or 13) and minutes<=60:
        print("lunch time")
    elif hours==(18 or 19) and minutes<=60:
        print("dinner time")



if __name__ == "__main__":
    main()
