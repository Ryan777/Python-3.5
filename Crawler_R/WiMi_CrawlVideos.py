#coding=utf-8
import requests
from bs4 import BeautifulSoup
import re

pattern = re.compile(r'\d{14}')
start_time = 20160721000000


for page in range(1,30):
    response = requests.get('http://ws.static.bfile.cloud.golomee.com/static/videos/ws/'+str(page)+'/')
    soup = BeautifulSoup(response.text,"html.parser")

    # links = soup.select('a[href^=/rlive]')
    files = [a.attrs.get('href') for a in soup.select('a[href^=rlive.live.media_hd]')]
    print(files)

    with open('Videos by Aug 8th.txt','a') as f:
        # f.writelines(links)
        # f.write('hello')
        for file in files:
            result = re.findall(pattern, file)
            if int(result[0])>20160721000000:
                print("True")
                # links.append('http://ws.static.bfile.cloud.golomee.com/static/videos/ws/5/'+f)
                link = 'http://ws.static.bfile.cloud.golomee.com/static/videos/ws/'+str(page)+'/'+file
                f.write(link)
                f.write('\n')
            else:
                continue