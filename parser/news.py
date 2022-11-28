from pprint import pprint

import requests
from bs4 import BeautifulSoup as BS

URL = 'https://kaktus.media/?lable=7650'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
}


def get_html(url, params=''):
    req = requests.get(url=url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='Tag--articles')
    news = []
    for item in items:
        news.append({
            'title': item.find('a', class_="ArticleItem--name"),
            'link': item.find('a', class_="ArticleItem--name").get('href'),
            'info': item.find('div', class_="ArticleItem--date").find('div').string
        })
    pprint(news)


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        news = []
        for i in range(1, 12):
            html = get_html(f'{URL}&page={i}')
            current_page = get_data(html.text)
            news.extend(current_page)
        return news

    else:
        raise Exception('Error in parser!')


a = parser()
print(len(a))
pprint(a)
