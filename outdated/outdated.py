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
while True:
    date=input("Date:")
    d1=date.split(" ")
    if d1[0].isalpha():
        if 
        for i in month:
            if i==d1[0]:
                month1=month[i]
        day1=d1[1].strip(",")
        year1=d1[-1]
        if int(day1)<=31 :
            if int(day1)<=9:
                day1="0"+day1
        else:
            continue
        print(year1+"-"+month1+"-"+day1)
    else:
        d2=date.split("/")
        if int(d2[0])<=12 :
            if int(d2[0])<=9:
                d2[0]="0"+d2[0]
        else:
            continue
        if int(d2[1])<=31 :
            if int(d2[1])<=9:
                d2[1]="0"+d2[1]
        else:
            continue
        print(d2[2]+"-"+d2[0]+"-"+d2[1])
    break




