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
    date=input("Date:")
    for i in date:
        for j in month:
            if i==j:
                date1[1]=month[j]
        print(i)
        print(date[1])
    break




