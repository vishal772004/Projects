import sys
from pyfiglet import Figlet
figlet=Figlet()
fonts=figlet.getFonts()

if sys.argv[1]=="-f" or sys.argv[1]=="--font":
    text=input("Input:")
    text=figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(text))
else:

    print("Invalid usage")
    sys.exit
