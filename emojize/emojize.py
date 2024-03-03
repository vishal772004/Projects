import requests
#emo=input("Input:").split()
req=requests.get("https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias")
print(req.json())
