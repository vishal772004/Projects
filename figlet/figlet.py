def main():
    import sys
    import pyfiglet

    if sys.argv[1]=="-f" or sys.argv[1]=="--font" :
        text=input("Input:")
        text=pyfiglet.figlet_format(text,font=sys.argv[2])
        print(text)

    print("Invalid usage")
    sys.exit(0)
main()
