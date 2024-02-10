def main():
    time=input("What time is it?")
    convert(time)


def convert(time):
    hours,minutes=time.split(":")
    hours=int(hours)
    minutes=int(minutes)
    if hours==7 and hours==8 and minutes<=60:
        print("breakfast time")
    elif hours==12 and hours==13  and minutes<=60:
        print("lunch time")
    elif hours==18 and hours==19 and minutes<=60:
        print("dinner time")



if __name__ == "__main__":
    main()
