def main():
    import sys
    import pyfiglet

    if sys.argv[1]=="-f" or sys.argv[1]=="--font" :
        text=input()
        text=pyfiglet.figlet_format(text,font=sys.argv[2])
        print(text)
    else:
        print("Invalid usage")
    sys.exit(1)
main()
