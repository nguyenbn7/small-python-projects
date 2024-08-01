import logging
import sys
import webbrowser
from urllib.parse import quote_plus

import bs4
import requests

logging.basicConfig(level=logging.DEBUG)

print("Googling...")
headers = {
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82",
}
res = requests.get(
    "http://google.com/search",
    params={"q": quote_plus(" ".join(sys.argv[1:]))},
    headers=headers,
)

logging.debug(res.url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")
search = soup.find(id="rso")
logging.debug(f"\n{search.prettify()}\n")

link_elems = search.select("a[aria-label]")
logging.debug(f"\n{link_elems}\n")

num_open = min(5, len(link_elems))

for i in range(num_open):
    logging.debug(f'{link_elems[i].get("href")}\n')
    webbrowser.open(link_elems[i].get("href"))
