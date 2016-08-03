#coding=utf-8
import requests
from bs4 import BeautifulSoup

for page in range(1,30):
    response = requests.get('http://ws.static.bfile.cloud.golomee.com/static/videos/ws/'+str(page)+'/')
    soup = BeautifulSoup(response.text,"html.parser")

    # links = soup.select('a[href^=/rlive]')
    files = [a.attrs.get('href') for a in soup.select('a[href^=rlive]')]


    with open('test.txt','a') as f:
        # f.writelines(links)
        # f.write('hello')
        for file in files:
            # links.append('http://ws.static.bfile.cloud.golomee.com/static/videos/ws/5/'+f)
            link = 'http://ws.static.bfile.cloud.golomee.com/static/videos/ws/'+str(page)+'/'+file
            f.write(link)
            f.write('\n')