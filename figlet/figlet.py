import sys
from pyfiglet import Figlet
figlet=Figlet()
fonts=figlet.getFonts()

if sys.argv[1]!="-f" or sys.argv[1]!="--font":
    print("Invalid usage")
    sys.exit

