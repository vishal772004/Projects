
text = input("Text:")

wordcount = 0
lettercount = 0
sentencecount = 0
for i in text.split():
    wordcount = wordcount+1
    for j in i:
        if(j.isalpha()):
            lettercount = lettercount+1
        if(j=='.' or j=='!' or j=='?'):
            sentencecount = sentencecount+1

L = lettercount/wordcount*100
S = sentencecount/wordcount*100

grade = 0.0588 * L - 0.296 * S - 15.8
if (grade<1):
    print("Before Grade 1")
elif (grade>=16):
    print("Grade 16+")
else:
    print("Grade",grade)



