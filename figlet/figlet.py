def main():
    import sys
    from pyfiglet import Figlet
    figlet=Figlet()
    font=figlet.getFonts()

    if sys.argv[1]=="-f" or sys.argv[1]=="--font":
        text=input("Input:")
        text=figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(text))
    else:

        print("Invalid usage")
        sys.exit
if __name__==__init__:
    main()
