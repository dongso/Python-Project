#module : 함수나 변수 또는 클래스들을 묶어놓은 파일(.py)
#Class -> Template
#클래스=붕어빵기계, 객체=붕어빵, 변수(속성)=길이,너비,내용물,색상...
#함수(메서드, 동작)=붕어빵을 굽는"일"


#import : 모듈 불러오기

from bs4 import BeautifulSoup
import urllib.request as req
html="""
<html><body>
<h1> 스크래핑</h1>
<p> 웹 페이지 분석 </p>
<p>부분 추출</p>
<h1>next</h1>
</body></html>
"""

#html 문서 분석
#BeautifulSoupt(분석할문서객체, parser)
soup=BeautifulSoup(html,'html.parser')
#BeautifulSoup : html, xml 문서를 분석할 수 있는 다양한 함수들이 제공됨
#생성자함수(클래스이름과 동일) : 객체를 생성할 때 호출하는 특별한 의미의 함수
#셍성자 함수를 호출해야 객체가 생성됨.
#만들어진 객체를 통해 클래스가 가지고 있던 함수나 변수 등을 사용할 수 있게 됨.

v1=soup.html.body.h1
print(v1)
print(v1.string) #<h1>태그에 포함된 순수 텍스트만 출력됨

#태그 이름을 점(.)으로 구분하여 나열

vp= soup.html.body.p
print(vp.string)
vp=vp.next_sibling #줄바꿈 문자가 들어가게 됨
vp=vp.next_sibling #따라서, next_sibling을 두번 해줘야됨
print(vp.string)

v4=soup.h1 #html.body ...이 아니고 바로 접근해도 됨.
print(v4.string)

print("*"*50)
v5=soup.p
print(v5.string)
v6=v5.next_sibling.next_sibling
print(v6.sting)

print("="*100)
html="""
<html><body>
<h1 id="title"> 스크래핑</h1>
<p id="mybody"> 웹 페이지 분석 </p>
<p id="mybody2">부분 추출</p>
</body></html>
"""
#find()::id 속성의 값을 통해 데이터를 추출하는 함수
soup=BeautifulSoup(html,'html.parser')
res=soup.find(id="title")
res1=soup.find(id="mybody")
res2=soup.find(id="mybody2")
print(res.string, res1.string, res2.string)

print("="*100)
html="""
<html><body>
<ul> <!-- unordered list-->
<li><a href="http://www.naver.com">naver</a></li>
<li><a href="http://www.daum.net">daum</a></li>
</ul>
</body></html>
"""
#Attribute의 값을 추출해보자
soup=BeautifulSoup(html,'html.parser')
links=soup.find_all("a") # 태그검색 출력결과 -> list
print(links)
#find: 한 개를 찾을때
#finde_all : 태그에 해당하는 전체 데이터를 가져올때
for i in links:
    href=i.attrs['href']
    text=i.string
    print(text,'==>',href)





#HTML : 비구조적=> 해독불가능 / XML: 구조적=> 해독가능
#mw-content-text > div > ul:nth-child(6) > li

print("="*100)

import urllib.request as req
url='http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'
res=req.urlopen(url)
print(res)
soup=BeautifulSoup(res,"html.parser") #httpResponse 객체를 html.parser를 사용해서 불러옴
title=soup.find("title")
print(title.string)

print("="*100)



