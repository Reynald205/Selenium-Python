import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 1
    while page <= max_pages:  # Will crawl though the page until max_page is reached.
        url = 'https://www.vprecords.com/albums/page/'+str(page)
        source_code = requests.get(url)
        plain_text = source_code.text  # Will store all the text in source code
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.find_all('a', {'class': "entry-link"}):
            href = link.get('href')
            title = link.string
            #print(href)
            #print(title)
            get_single_item_data(href)
            page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text  # Will store all the text in source code
    soup = BeautifulSoup(plain_text, "html.parser")
    for page_title in soup.find_all('h1',{'class':'page-title'}):
        print(page_title.string)

trade_spider(4)
