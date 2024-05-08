def convert(str):
        if ":)" in str:
            str= str.replace(":)","\U0001F642")
        if ":(" in str:
             str= str.replace(":(","\U0001F641")

        print(str)


def main():
    phrase=input("Enter any phrase:")

    convert(phrase)

main()

