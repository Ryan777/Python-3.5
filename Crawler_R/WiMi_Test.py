import requests
from bs4 import BeautifulSoup

responses = requests.get('http://ws.static.bfile.cloud.golomee.com/static/videos/ws/24/')
soup = BeautifulSoup(responses.text,"html.parser")
print(soup)