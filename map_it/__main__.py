import logging
import sys
import webbrowser
from urllib.parse import quote_plus, urljoin

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")

if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])
else:
    raise Exception("Address not found")

url = urljoin("https://www.google.com/maps/place/", quote_plus(address))
logging.debug(url)
webbrowser.open(url)
