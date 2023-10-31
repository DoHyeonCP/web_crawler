from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
except HTTPError as e: # 페이지를 찾을 수 없거나, URL 해석에서 에러가 생긴 경우
    print(e)
except URLError as e: # 서버를 찾을 수 없을 때
    print('The server could not be found!')
else: # except에서 null을 반환하거나, break문을 실행하거나, 기타 다른 방법을 사용할 경우 없어도 됨.
    print('It Worked')

# 아래와 같은 범용함수를 만들고 예외처리를 철저하게 만들어 놓아야한다.
def getBadContent(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        #nonExistingTag는 none을 반환
        #none 객체에 어떤 함수를 호출할 경우 AttributeError 발생
        badContent = bs.nonExistingTag.anotherTag
    except AttributeError as e:
        return None
    return badContent

badContent = getBadContent("http://pythonscraping.com/pages/page1.html")

if badContent == None:
    print('Title could not be found')
else:
    print(badContent)