import re

def main():
    print(count(input("Text: ")))


def count(s):
    counting=0
    words=s.split()
    for i in words:
        if re.search("(um|Um)",i):
            counting=counting+1
    return counting


if __name__ == "__main__":
    main()
