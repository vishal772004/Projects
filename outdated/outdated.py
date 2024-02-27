month={
    "January":"01",
    "February":"02",
    "March":"03",
    "April":"04",
    "May":"05",
    "June":"06",
    "July":"07",
    "August":"08",
    "September":"09",
    "October":"10",
    "November":"11",
    "December":"12"
}
date1=[]
while True:
    date=input("Date:")
    d1=date.split(" ")
    if d1[0].isalpha():
        for i in month:
            if i==d1[0]:
                month1=month[i]
        day1=d1[1].strip(",")
        year1=d1[-1]
        print(year1+"-"+month1+"-0"+day1)
    else:
        d2=date.split("/")
        print(d2[2]+"-0"+d2[0]+"-0"+d2[1])
    break




