import requests
from bs4 import BeautifulSoup
import csv

CSV = 'phones.csv'
HOST = 'https://alfa.kz/'
URL = 'https://alfa.kz/phones/telefony-i-smartfony'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}


def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_dl(soup):
    keys, values = [], []
    for dl in soup.findAll("dl", {"class": "dl-horizontal"}):
        for dt in dl.findAll("dt"):
            keys.append(dt.text.strip())
        for dd in dl.findAll("dd"):
            values.append(dd.text.strip())
    dd = dict(zip(keys, values))
    return dd


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='row product-item product-item-holder')
    phones = []
    phone_info = []

    for item in items:
        phones.append(
            item.findNext('div', class_='title').find('a').get('href')
        )

    for phone in phones:
        html_phone = get_html(phone).text
        soup_phones = BeautifulSoup(html_phone, 'html.parser')
        items_phones = soup_phones.find_all('div', id='single-product', class_='container')
        dl_dict = get_dl(soup_phones)
        for n in items_phones:
            phone_info.append(
                {
                    'title': n.findNext('div', class_='col-xs-12 col-sm-9').find(class_='col-xs-12 col-sm-6 pull-right title single-product-title').text.strip(),
                    'price': n.findNext('div', class_='price-container').find('span', class_='num').text.strip(),
                    'seller': n.findNext('div', class_='panel-body').find('a').text.strip(),
                    'ram': dl_dict.get('Оперативная память'),
                    'memory': dl_dict.get('Встроенная память')
                }
            )

    return phone_info


def save_doc(items, path):
    with open(path, "w", encoding="utf-8-sig", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['title', 'price', 'seller', 'ram', 'memory'])
        for item in items:
            writer.writerow([item['title'], item['price'], item['seller'], item['ram'], item['memory']])


def parser():
    check_html = get_html(URL)
    if check_html.status_code == 200:
        phones = []
        phones.extend(get_content(check_html.text))
        save_doc(phones, CSV)
    else:
        print('Error')


parser()

