from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(html, 'html.parser')
# 람다를 사용할 경우 반드시 태그 객체를 매개변수로 받아야하고, 불리언만 반환할 수 있다
# 속성이 정확히 두 개인 태그 가져오기
bs.findAll(lambda tag: len(tag.attrs) == 2)