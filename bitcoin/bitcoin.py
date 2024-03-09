import requests
import sys
import math
temp=""
price=0.0
try:
    for i in sys.argv[1]:
        temp=temp+i
    y=temp.index(".")
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
    s=details['bpi']['USD']['rate'].split(".")
    for i in s:
        if i==",":
            continue
        price=price+(float(i)*)


except requests.RequestException:
    sys.exit()

