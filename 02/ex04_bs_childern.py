from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(html, 'html.parser')

# 자식만 찾아주는 .children, 만약 붙이지 않았다면 table의 자손들은 전부 출력되었을 것이다.
for child in bs.find('table', {'id': 'giftList'}).children: #giftList테이블에 있는 제품행 목록 출력
    print(child)