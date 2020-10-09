import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

soup1 = BeautifulSoup(page.content, 'html.parser')

print("---------------------")

print(soup1.prettify())