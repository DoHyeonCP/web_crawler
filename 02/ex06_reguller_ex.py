# * : 바로 앞에 있는 문자, 하위 표현식, 대괄호로 묶인 문자들이 0번이상 나타납니다.
# + : 바로 앞에 있는 문자, 하위 표현식, 대괄호로 묶인 문자들이 1번이상 나타납니다.
# [] : 대괄호 안에 있는 문자 중 하나가 나타납니다 ex: [A-Z]
# () : 그룹으로 묶인 하위 표현식. 정규 표현식을 평가할 때에는 하위 표현식이 가장 먼저 평가
# {m, n} : 바로 앞에 있는 문자, 하위 표현식, 대괄호로 묶인 문자들이 m번이상 n번 이하 나타납니다.
# | : | 로 분리된 문자, 문자열, 하위 표현식 중 하나가 나타납니다.
# . : 문자 하나(글자, 숫자, 기호, 공백 등)가 나타납니다.
# ^ : 바로 뒤에 있는 문자 혹은 하위 표현식이 문자열의 맨 앞에 나타납니다.
# \ : 특수 문자를 원래 의미대로 쓰게하는 이스케이프 문자입니다.
# $ : 문자 또는 하위 표현식이 문자열의 마지막 이라는 뜻. 이 기호를 쓰지 않으면 사실상 마지막에 .*가 마지
# 막에 있는 거나 마찬가지
# ?! : '포함하지 않는 다는 뜻  이 기호 쌍 바로 다음에 있는 문자(또는 하위 표현식)는 해당 위치에 나타나지
# 않습니다. 특정 문자를 완벽히 배제하려면 ^과 $를 앞뒤에 작성

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re # 정규식 표현

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(html, 'html.parser')
images = bs.findAll('img', {'src': re.compile('\.\.\/img\/gifts/img.*\.jpg')})
for image in images:
    print(image['src'])

## 추가적으로 태그의 속성에 관심이 있을 대 myTag.attrs['src'] 를 통해 속성에 접근
