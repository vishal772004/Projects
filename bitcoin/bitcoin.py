import requests
import sys
temp=""
for i in sys.argv[1]:
    temp=temp+i
try:
    if temp.find(".")>0 or temp.isdigit():
        pass
except ValueError:
    sys.exit()
try:
    
except requests.RequestException:
    ...
