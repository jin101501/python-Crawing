# import requests
# from bs4 import BeautifulSoup
from urllib.request import urlopen #urllib.request 모듈은 URL 이나 HTTP를 여는 데 도움이 되는 함수와 클래스를 정의한다. urlopen은 string이나 Request 객체인 URL을 열어준다.
from bs4 import BeautifulSoup # 웹 페이지의 정보를 추출하기 위한  beautifulsoup4 모듈
import re

url = [
    "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EA%B0%9C%EB%B0%9C%EC%9E%90&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=36&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=1",
    "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EA%B0%9C%EB%B0%9C%EC%9E%90&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=54&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=11"
]
# 페이지에서의 URL 호출(URL 주소에서 해당되는 부분의 주소가 호출된다.)
def UrlList():
    urlList=[]
    for val in url:
        html = urlopen(val)
        bsObject = BeautifulSoup(html, "html.parser")
        for link in bsObject.find_all('a',{'class':'news_tit'}):
            urlList.append(link.get('href'))    
    print(urlList)           
    return urlList
# def UrlList():
#     urlList=[]
#     for val in url:
#         html = urlopen(val)
#         bsObject = BeautifulSoup(html, "html.parser")
#         for link in bsObject.find_all('a',{'class':'news_tit'}):
#             urlList.append(link.get('href'))    
#     #print(urlList)           
#     return urlList

# def UrlText():
#     urlList = UrlList()
#     textList = []
    
#     for val in urlList:
#         try:
#             html = urlopen(val)
#             bsObject = BeautifulSoup(html, "html.parser")
#             for data in bsObject.select('p,div'):
#                 #줄바꿈, 탭은 공란 처리
#                 textList.append(re.sub('\n|\t','',data.text.strip()))
#         except:
#             print("URL Error :", val)
#     # print(textList)
#     return textList


# raw = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=U20", headers = {"User-Agent" : "Mozilla/5.0"})

# print(raw)

# html  = BeautifulSoup(raw.text,"html.parser")
# print(html.title)

# container = html.select("ul.list_news >li")
# print(container)

# title = container[0].select_one("#sp_nws1 > div.news_wrap.api_ani_send > div > a").text

# print(title)

# for i in range(0,10):
#     title = container[i].select_one("#sp_nws1 > div.news_wrap.api_ani_send > div > a").text
#     print(title)