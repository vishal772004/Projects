import requests
import sys
temp=""
try:
    for i in sys.argv[1]:
        temp=temp+i
    if temp.find(".")>0 or temp.isdigit():
        pass
except ValueError:
    sys.exit()
except IndexError:
    print("Missing Command-line Argument")
try:
    details=requests.get()
    print(details)
except requests.RequestException:
    sys.exit()
