import emoji
emo=(input("Input:")).split()
for i in emo:
    if i.startswith(":"):
        print(emoji.emojize(i),language='alias')
    else:
        print(i)

