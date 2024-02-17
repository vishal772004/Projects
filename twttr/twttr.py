phrase=input("Input:").split()
for str in phrase:
    str=str.upper()
    if str=="A" or str=="E" or str=="I" or str=="O" or str=="U":
        str=str.replace(str,"")
        print(str)
print("Output:",phrase)


