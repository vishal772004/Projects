
def main():
    phrase=input("Input:")
    l=[]
    for i in phrase:
        l.append(i)
    print(shorten(phrase))
def shorten(word):
    vowels=["A","E","I","O","U","a","e","i","o","u"]
    for i in word:
        for j in vowels:
            if i==j:
                word=word.replace(i,"")
    return word

