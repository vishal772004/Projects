import requests
from bs4 import BeautifulSoup

def main():
    response = requests.get('http://www.imdb.com/chart/top')
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup)
def function_1():
    ...


def function_2():
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()
