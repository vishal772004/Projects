import requests
emo=input("Input:").split()
req=requests.get("https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias")
for i in emo:
    if i==req:
        print(req)
