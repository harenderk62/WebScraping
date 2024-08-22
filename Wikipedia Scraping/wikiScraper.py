import requests
from bs4 import BeautifulSoup

page = requests.get("https://en.wikipedia.org/wiki/Main_Page")

soup = BeautifulSoup(page.content, 'html.parser')

object = soup.find(id="mp-left")

items = object.find_all(class_="mp-h2")
result = items[0]

print(result.prettify())