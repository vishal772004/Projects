import requests
import sys
import math
temp=""
price=0.0
try:
    for i in sys.argv[1]:
        temp=temp+i
    y=temp.index(".")
    if y>0 or temp.isdigit():
        pass
except ValueError:
    sys.exit()
except IndexError:
    print("Missing Command-line Argument")
try:
    z=0
    y=0
    details=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    print(details['bpi']['USD']['rate'])
    for i in details['bpi']['USD']['rate']:
        if i==",":
            continue
        elif i==".":
            z=z+1
            continue
        else:
            price=price*math.pow(10,y)+(float(i))
            print(price)
            y=y+1

except requests.RequestException:
    sys.exit()

