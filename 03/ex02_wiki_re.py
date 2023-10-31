# 항목 페이지를 가리키는 링크에는 다른 내부 페이지를 가리키는 링크와비교되는 세 가지 공통점
# 1. id가 bodyContent인 div 안
# 2. URl에는 콜론이 없음
# 3. URL은 /wiki/로 시작됨
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find('div', {'id':'bodyContent'}).findAll('a',
                    href = re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])
