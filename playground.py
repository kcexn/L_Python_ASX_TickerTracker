#!/home/kevin/.local/share/virtualenvs/ASX_tickerTracker-1IztkTdb/bin/python3
from lxml import html
import requests

page = requests.get('https://en.wikipedia.org/wiki/Blog')
tree = html.fromstring(page.content)
first_heading = tree.xpath('//*[@id="firstHeading"]/text()')
print(first_heading)
