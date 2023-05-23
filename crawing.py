import requests
from bs4 import BeautifulSoup

raw = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=U20", headers = {"User-Agent" : "Mozilla/5.0"})

# print(raw)

html  = BeautifulSoup(raw.text,"html.parser")
# print(html.title)

container = html.select("ul.list_news >li")
# print(container)

# title = container[0].select_one("#sp_nws1 > div.news_wrap.api_ani_send > div > a").text

# print(title)

for i in range(0,10):
    title = container[i].select_one("#sp_nws1 > div.news_wrap.api_ani_send > div > a").text
    print(title)