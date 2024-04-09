import requests
from bs4 import BeautifulSoup

def main():
    response = requests.get('http://www.imdb.com/chart/top')
    soup = BeautifulSoup(response.text, "html.parser")
    movies = soup.select('td.titleColumn')
    crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
    ratings = [b.attrs.get('data-value')
        for b in soup.select('td.posterColumn span[name=ir]')]
    print(movies)
    https://github.com/ExplorerMunchkin/web-scraping-imdb-top250-python/raw/main/IMDBTop250.csv
def function_1():
    ...


def function_2():
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()
