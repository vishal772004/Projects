phrase=input("Input:").split()
vowels=["A","E","I","O","U","a","e","i","o","u"]
for i in phrase:
    for k in vowels:
        if i==k:
            phrase.replace(i," ")
print(phrase)
