import sys
if sys.argv[1]!="-f" or sys.argv!="--font":
    print("Invalid usage")
    sys.exit
print("Hello",sys.argv[1])
