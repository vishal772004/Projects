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
    d1=date.split(" ")
    print(d1)
    
    d2=date.split("/")
    day2=d2[1]
    month2=d2[0]
    year2=d2[2]
    print(year2+"-0"+month2+"-0"+day2)

    print(date)
    break




