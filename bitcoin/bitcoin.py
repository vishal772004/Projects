import requests
import sys
import math
temp=""
price=0.0
try:
    for i in sys.argv[1]:
        temp=temp+i
    y=temp.find(".")
    print(y)
    if y>0 or temp.isdigit():
        pass
except ValueError:
    sys.exit()
except IndexError:
    print("Missing Command-line Argument")
try:
    z=0
    details=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    for i in details['bpi']['USD']['rate']:
        if i==",":
            continue
        if i==".":
            z=z+1
            continue
        if z>0:
            price=price+(float(i)*math.pow(10,-z))
            z=z+1
        else:
            price=price+(float(i)*math.pow(10,y))
            y=y-1

except requests.RequestException:
    sys.exit()

