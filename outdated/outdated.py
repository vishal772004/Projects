month={
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}
date1=[]
while True:
    date=input("Date:").split("/")
    for i in date:
        if date[0]==i :
            for j in month:
                if i==j:
                    date1[1]="0"+month[j]
        elif date[0]==i and date[0]<=12:
            date[1]="0"+i
        else:
            continue
        print(date1)
        break




