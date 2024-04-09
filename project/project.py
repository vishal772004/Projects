import requests


def main():
    response = requests.get('http://www.imdb.com/chart/top')
    reader = response.json()
    print(reader)
def function_1():
    ...


def function_2():
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()
