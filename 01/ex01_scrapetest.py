from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page1.html")

# http://pythonscraping.com에 있는 서버의 /pages 디렉터리의 HTML, page1.html 출력
print(html.read())

