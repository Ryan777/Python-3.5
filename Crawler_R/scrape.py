#coding=utf-8
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
# print(html.read())
bsObj = BeautifulSoup(html.read(),"html.parser")
# bsObj = BeautifulSoup(html)
# print(bsObj)

# nameList = bsObj.findAll('span',{'class':'green'})
#
# for name in nameList:
#     print(name.text)  # name.get_text() , differences?

nameList = bsObj.findAll(text = 'prince')
print(len(nameList))