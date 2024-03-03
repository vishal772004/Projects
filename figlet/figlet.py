def main():
    import sys
    from pyfiglet import Figlet
    print(Figlet.getFonts())

    if sys.argv[1]=="-f" or sys.argv[1]=="--font":
        text=input("Input:")
        text=Figlet.setFont(f=sys.argv[2])
        print(Figlet.renderText(text))
    else:

        print("Invalid usage")
        sys.exit
main()
