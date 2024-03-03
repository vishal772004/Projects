def main():
    import sys
    import pyfiglet
    f=pyfiglet.FigletFont.getFonts()
    z=0
    for i in f:
        if i==sys.argv[2]:
            z=1
    if z!=1:
        sys.exit(1)

    if sys.argv[1]=="-f" or sys.argv[1]=="--font":
        text=input()
        text=pyfiglet.figlet_format(text,font=sys.argv[2])
        print(text)
        sys.exit(0)
    else:
        print("Invalid usage")
        sys.exit(1)
main()
