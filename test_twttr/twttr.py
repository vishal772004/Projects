phrase=input("Input:")
l=[]
for i in phrase:
    l.append(i)
vowels=["A","E","I","O","U","a","e","i","o","u"]
for i in phrase:
    for j in vowels:
        if i==j:
            phrase=phrase.replace(i,"")
print("Output:",phrase)
