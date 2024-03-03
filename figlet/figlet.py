def main():
    import sys
    import pyfiglet

    if sys.argv[1]=="-f" or sys.argv[1]=="--font":
        text=input("Input:")
        text=pyfiglet.figlet_format(text,f=sys.argv[2])
        print(text)
    else:

        print("Invalid usage")
        sys.exit
main()
