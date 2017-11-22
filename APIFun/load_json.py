import urllib.request
import json
from bs4 import BeautifulSoup
from pprint import pprint

urlData = "https://api.coinmarketcap.com/v1/ticker/?convert=USD&limit=5"
webURL = urllib.request.urlopen(urlData)
data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
crypto_list = json.loads(data.decode(encoding))

print(crypto_list)
first_elem = crypto_list[0]
print(first_elem)
