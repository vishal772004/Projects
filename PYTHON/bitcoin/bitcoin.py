import requests
import sys
import math
price=0.0
try:
    n=float(sys.argv[1])
except ValueError:
    print("Command line argument is not a number")
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
        elif z>0:
            price=price+(float(i)*math.pow(10,-z))
            z=z+1
        else:
            price=(price*10)+float(i)
    print(f"${price*n:,.4f}")


except requests.RequestException:
    sys.exit()

