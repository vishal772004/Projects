camelCase=input("Camel Case:");
for i in camelCase:
    if i.isupper():
        camelCase=camelCase.replace(i,"_"+i.lower())
print("Snake case:",camelCase)
