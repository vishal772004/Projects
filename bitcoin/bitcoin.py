import requests
import sys
import math
temp=""
price=0.0
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
try:
    z=0
    details=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    s=details['bpi']['USD']['rate'].split(".")
    for i in s:
        price=price+float(i)

    print("$",price*sys.argv[1])
except requests.RequestException:
    sys.exit()
