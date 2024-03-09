import requests
import sys
import math
temp=""
price=[]
try:
    for i in sys.argv[1]:
        temp=temp+i
    if temp.find(".")>0 or temp.isdigit():
        pass
except ValueError:
    sys.exit()
except IndexError:
    print("Missing Command-line Argument")
    z,y=0
try:
    details=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    for i in details['bpi']['USD']['rate']:
        if i=="." or z>0:
            z=z+1
            price=price+(float(i)*(math.pow(10,-z)))
        else:
            
            price=price+(float(i))
    print("$",price*sys.argv[1])
except requests.RequestException:
    sys.exit()
