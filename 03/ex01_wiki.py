from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
for link in bs.findAll('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])

# 하지만 위에처럼 하면 관심이 없는 많은 링크가 섞여들어옴



