# web crawler basic using beautifulsoup 4
import requests
from bs4 import BeautifulSoup

URL = 'https://theguardian.com/uk'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
