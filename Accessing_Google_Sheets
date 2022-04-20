!pip install bs4

# Importing libaries
from urllib.request import urlopen, urlretrieve, Request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import pandas as pd

# Getting HTML
url = "https://datastudio.google.com/s/psUd8E5JHsQ"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ApplewebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}

req = Request(url,headers=headers)
response = urlopen(req)
html = response.read()
soup = BeautifulSoup(html,'html.parser')

#Getting necesseries Tags
list_ = soup.find('table')
