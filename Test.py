#coding=utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page1.html")
# print(html.read())
bsObj = BeautifulSoup(html.read())
print(bsObj.h1)