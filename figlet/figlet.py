import sys
from pyfiglet import Figlet
figlet=Figlet()
fonts=figlet.getFonts()

if sys.argv[1]!="-f" or sys.argv[1]!="--font":
    print("Invalid usage")
    sys.exit
else:
    text=input("Input:")
    text=figlet.setFont(font=argv[2])
    print(figlet.renderText(text))
