# #정규표현식을 그룹으로 묶는 방법:패턴 내부에서 정규표현식을 괄호로 묶으면 그룹이 됨
# #예) (정규표현식)
# import re
# pat=re.match("([0-9]+) ([0-9]+)", "10 295")#괄호로 묶였으므로 그룹이 됨
# print(pat)
# print(pat.group(1)) #1번째 그룹에 매칭된 문자열을 출력
# print(pat.group(2)) #2번째 그룹에 매칭된 문자열을 출력
# print(pat.group()) #전체 그룹에 매칭된 문자열을 출력
# print(pat.group(0)) #전체 그룹에 매칭된 문자열을 출력
#
# print(pat.groups()) #각 그룹에 해당되는 문자열을 튜플 형태로 출력
# #그룹의 구분을 숫자가 아닌 이름으로 할 수 있음
# #그룹 이름은 괄호 안에 ?P<그룹이름>   형식으로 작성
# m=re.match("(?P<func>[a-zA-Z_][a-zA-Z0-9_]+)", "print(1234)")#함수이름은 영문으로 시작, 숫자도 포함
# print(m)
# print(m.group(1))
# print(m.group("func"))
#
#
# print("="*50)
#
# m=re.match("(?P<func>[a-zA-Z_][a-zA-Z0-9_]+)\((?P<arg>\w+)\)", "print(1234)")#함수이름은 영문으로 시작, 숫자도 포함
# print(m)
# print(m.group(1))
# print(m.group("func"))
# print(m.group(2))
# print(m.group("arg"))
#
# print(re.match("[0-9]+", "1 2 buzz 3 4 fizz 5 6"))
# print(re.search("[0-9]+", "1 2 buzz 3 4 fizz 5 6"))
# print(re.findall("[0-9]+", "1 2 buzz 3 4 fizz 5 6"))
# print(re.findall("[a-z]+", "1 2 buzz 3 4 fizz 5 6"))
#
#
# #우리나라 코리아 korea 한국 대한민국 조선 ... => 대한민국
# #형식 : re.sub("패턴", "바꿀문자열", "문자열", 바꿀횟수)
# #바꿀횟수를 생략하면 모든 문자열을 바꿈
# #"패턴"에 해당하는 "문자열"을 "바꿀문자열"로 "바꿀횟수"만큼 바꿔라
# print(re.sub("apple|orange","fruit","apple box orange box"))
# #apple 또는 orange 를 fruit로 바꿔라
#
# #"1 2 fizz 4 buzz fizz 7 8 99"  숫자만 찾아서 n으로 변경
# #"n n fizz n buzz fizz n n n"
# print(re.sub("[0-9]+","n", "2 fizz 4 buzz fizz 7 8 99"))
# print(re.sub("[0-9]+","n", "2 fizz 4 buzz fizz 7 8 99", 3))
#
# #형식 : re.sub("패턴", 함수, "문자열", 바꿀횟수)
# print("="*50)
# print(re.sub("[0-9]+",lambda m: str(int(m.group())+10), "2 fizz 4 buzz fizz 7 8 99"))
#
# def myRpl(m):
#     n=int(m.group())
#     return str(n+10)
#
# print(re.sub("[0-9]+",myRpl, "2 fizz 4 buzz fizz 7 8 99"))
#
#
#

from bs4 import BeautifulSoup
import urllib.request as req
url="https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=103&oid=056&aid=0010687903"
res=req.urlopen(url)
#print(res)
soup=BeautifulSoup(res, 'html.parser')
print(soup)
article=soup.select_one("#articleBodyContents").string
print(article)











