from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(html, 'html.parser')

nameList = bs.findAll('span', {'class': 'green'}) # <span class = "green" ... ></span>안에 든 모든 텍스트
for name in nameList:
    # get_text() 현재 문서에서 모든 테그를 제거하고 유니코드 텍스트들만 들어있는 문자열 반환
    # 항상, 마지막, 즉 최종 데이터를  출력하거나 저장, 조작하기 직전에만 써야 합니다.
    print(name.get_text())