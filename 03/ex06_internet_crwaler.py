from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now().timestamp())

# 페이지에서 발결된 내부 링크를 모두 목록으로 만듭니다.
def getInternalLinks(bs, includeUrl):
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme,
                                  urlparse(includeUrl).netloc)
    internalLinks = []
    # /로 시작하는 링크를 모두 찾습니다.
    for link in bs.findAll('a', href = re.compile('^(/|.*' + includeUrl + ')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] is not internalLinks:
                if(link.attrs['href'].startswith('/')):
                    internalLinks.append(includeUrl + link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])

    return internalLinks

# 페이지에서 발견된 외부 링크를 모두 목록으로 만듭니다.
def getExternalLinks(bs, excludeUrl):
    externalLinks = []
    # 현재 URL을포함하지 않으면서 http나 www로 시작하는 모든 링크를 모두 찾습니다.
    for link in bs.findAll('a',
                           href = re.compile('^(http|www)((?!' + excludeUrl + ').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def getRandomExternalLink(startingPage):
        html = urlopen(startingPage)
        bs = BeautifulSoup(html, 'html.parser')
        externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc)
        if len(externalLinks) == 0:
            print('No external links, looking around the site for one')
            domain = '{}://{}'.format(urlparse(startingPage).scheme,
                                      urlparse(startingPage).netloc)
            internalLinks = getInternalLinks(bs, domain)

            return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
        else:
            return externalLinks[random.randint(0, len(externalLinks)-1)]
        
def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print('Random external link is: {}'.format(externalLink))
    followExternalOnly(externalLink)

followExternalOnly('http://oreilly.com')


#### 추가적으로 사이트 전체에서 외부 링크를 검색하고 각 링크마다 메모를 남기고 싶다면 다음과 가은 함수 사용

allExtLinks = set()
allIntLinks = set()

def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    domain = '{}://{}'.format(urlparse(siteUrl).scheme,
                                urlparse(siteUrl).netloc)
    bs = BeautifulSoup(html, 'html.parser')
    internalLinks = getInternalLinks(bs, domain)
    externalLinks = getExternalLinks(bs, domain)

    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            allIntLinks.add(link)
            getAllExternalLinks(link)
    