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
  #  if date.isalnum():
    if int(d1[1])<=31:
        date1[2]=d1[1]
        print(date1[2])
    else:
        continue
    date1[0]=d1[-1]
    print(date1[0])
    for i in d1:
        for j in month:
            if i==j:
                date1[1]="0"+month[j]
    print(date1[1])
    break




