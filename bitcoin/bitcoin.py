import requests
import sys
import math
temp=""
price=[]
try:
    for i in sys.argv[1]:
        temp=temp+i
    y=temp.find(".")
    if y>0 or temp.isdigit():
        pass
except ValueError:
    sys.exit()
except IndexError:
    print("Missing Command-line Argument")
    z=0
try:
    details=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    for i in details['bpi']['USD']['rate']:
        if i=="." or z>0:
            z=z+1
            price=price+(float(i)*(math.pow(10,-z)))
        else:
            y=y-1
            price=price+(float(i)*(math.pow(10,y)))
    print("$",price*sys.argv[1])
except requests.RequestException:
    sys.exit()
