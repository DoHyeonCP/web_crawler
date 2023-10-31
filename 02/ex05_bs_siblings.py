from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(html, 'html.parser')

# 첫 번째 테이블에서 첫번째 타이틀 행을 제외한 모든 제품 출력
# 추가적으로 previous_siblings, next_sibling, previous_sibling이 있음
for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(sibling)