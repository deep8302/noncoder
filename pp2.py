#!/usr/bin/python3

import urllib.request

#from bs4.Beautifulsoup import Beautifulsoup

query=input("what you would like to search: ")

page = urllib.request.urlopen("https://www.google.dz/search?q=%s"%query)
soup = BeautifulSoup(page.read())
links = soup.findAll("a")
for link in links:
    print(link["href"])

'''
import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.google.dz/search?q=%s"%query)
soup = BeautifulSoup(page.content)
print(soup)
import re
links = soup.findAll("a")
for link in  linkss("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
    print (re.split(":(?=http)",link["href"].replace("/url?q=",""))""")
"""










