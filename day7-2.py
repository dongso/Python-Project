from bs4 import BeautifulSoup
import urllib.request as req
from urllib.parse import urljoin

import requests

# soupt.select_one(선택자):선택자 하나를 추출
# soup.select(선택자) : 선택자에 해당하는 여러 개의 요소를 리스트 형태로 추출

html="""
<html><body>
    <div id="book">
    <h1>어린왕자</h1>
    <ul class="items">
    <li>생떽쥐베리</li>
    <li>사막 불시창</li>
    <li>소년과 양</li>
    </ul>
    </div>
</body></html>
"""

#html 분석
soup=BeautifulSoup(html,'html.parser')
h1=soup.select_one("div#book > h1").string #작성형식 : 태그명#아이디 > 하위태그.클래스명 >...
print("제목=",h1)

#목록 추출
li_list=soup.select("div#book > ul.items > li") #.string -> ERROR ::list이기 때문에 for문을 사용해서 .string 적용할 것.
for li in li_list:
    print("목록=", li.string)


url="http://finance.naver.com/marketindex/"
res=req.urlopen(url)
soup=BeautifulSoup(res,'html.parser')
#print(soup)

usd=soup.select("div.head_info > span.value")
print("usd/kw=",usd)


myList=soup.select("a.head.eur> div > span.value")
print(myList)

#exchangeList > li:nth-child(1) > a.head.usd > div > span.value
#exchangeList > li.on > a.head.eur > div > span.value

url="https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
res=req.urlopen(url)
soup=BeautifulSoup(res,'html.parser')
bookTitle=soup.select_one("#mw-content-text > div > ul:nth-child(6) > li > b > a")
print(bookTitle.string)

s1=soup.select_one("#mw-content-text > div > ul:nth-child(6) > li > ul > li:nth-child(1) > a").string
print(s1)

s2=soup.select_one("#mw-content-text > div > ul:nth-child(6) > li > ul > li:nth-child(2) > a").string
print(s2)

myList=soup.select("#mw-content-text > div > ul:nth-child(6) > li > ul > li> a")
for mL in myList:
    print(mL.string)


url=("https://search.naver.com/search.naver?where=kin&sm=tab_jum&query=%EB%B8%94%EB%9E%99%ED%95%91%ED%81%AC")
res=req.urlopen(url)
soup=BeautifulSoup(res,'html.parser')
kinTitle=soup.select_one("#elThumbnailResultArea > li:nth-child(4) > dl > dt > a").string
#print(kinTitle)


print("*"*10+"HOME.html에서 꺼삐딴리 추출하기"+"*"*10)
#HOME.html에서 꺼삐딴리 추출하기
# id="title"
# id="id4"

with open('HOME.html','r',encoding='utf-8') as fp:
    soup=BeautifulSoup(fp,'html.parser')
    #print(soup)
    sel=lambda q:print(soup.select_one(q).string)
    sel("#id4")
    sel("li#id4")
    sel("ul > li#id4")
    sel("#title > li#id4")
    sel("#title #id4") #id안에 id
    sel("#title > #id4") #id > id
    sel("ul#title > li#id4")
    sel("li[id='id4']")
    sel("li:nth-of-type(4)")
    print(soup.select("li")[3].string)
    print(soup.find_all("li")[3].string)



#로그인이 필요한 사이트로부터 스크래핑

#로그인 => http://www.hanbit.co.kr/member/login.html
url="http://www.hanbit.co.kr/member/login.html"
res=req.urlopen(url)
soup=BeautifulSoup(res,'html.parser')

#아이디 => #m_id
#비밀번호 => #m_passwd
#마이한빛 => http://www.hanbit.co.kr/myhanbit/myhanbit.html
#마일리지 => #container > div > div.sm_mymileage > dl.mileage_section1 > dd > span
#코인 => #container > div > div.sm_mymileage > dl.mileage_section2 > dd > span
#로그인확인 => http://www.hanbit.co.kr/member/login_proc.php
#http://www.hanbit.co.kr/myhanbit/myhanbit.html <- 코인추출
#index.html > login_proc.php > index.html > myhanbit.html


USER=""
PASSWORD=""

#Server Connection
session=requests.session() #Session Object : 웹서버에 접속할 수 있도록 해주는 객체

login_info={ #로그인 정보를 딕셔너리 형태로 만들어서 post()를 통해 전달
    "m_id":USER,
    "m_passwd":PASSWORD
}
url_login="http://www.hanbit.co.kr/member/login_proc.php"
res=session.post(url_login,login_info)

url_mypage="http://www.hanbit.co.kr/myhanbit/myhanbit.html"
res=session.get(url_mypage)

soup=BeautifulSoup(res.text,'html.parser')
mileage=soup.select_one("#container > div > div.sm_mymileage > dl.mileage_section1 > dd > span").string
ecoin=soup.select_one("#container > div > div.sm_mymileage > dl.mileage_section2 > dd > span").string
print("mileage-> ",mileage," \nE coin->",ecoin)





#http://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K&maker_no=49&group_no=5&page=1&order=S11&view_size=20
#http://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K&maker_no=3&page=1&order=S11&view_size=20

#listCont > div.wrap-thumb-list > ul > li > div > div.mode-cell.fuel > span










