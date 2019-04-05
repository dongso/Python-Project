import re
# 문제1
# 다음과 같은 문자열에서 핸드폰 번호 뒷자리인 숫자 4개를 ####으로 바꾸는 프로그래미을 정규식을 이용하여 작성해보자
# park 010-9999-9988
# kim 010-9909-7789
# lee 010-8789-7768
phoneN={'park':'010-9999-9988',
        'kim':'010-9909-7789',
        'lee':'010-8789-7768'}
pnPat=re.compile('[0-9]{4}$')

for k,v in phoneN.items():
    v=v.replace()


# 문제2
# 다음은 이메일 주소를 나타내는 정규식이다.  이 정규식은 park@naver.com, kim@daum.net, lee@myhome.co.kr 등과
# 매치됨.
# 긍정형 전방 탐색 기법을 이용하여 com, net이 아닌 이메일 주소는 제외시키는 정규식을 작성해보자
# .*[@].*[.].*$

pat=re.compile('[-_.\w]+@[a-z-]+\.(com|net)') #@는 \를 안붙여도 된다.

emailList=['kim@daum.net','lee@myhome.co.kr']

for email in emailList:
    if None==pat.match(email):
        print("invalid email->",email)
print(emailList)



# 문제3
# 표준 입력으로 URL 문자열이 입력됩니다. 입력된 URL이 올바르면 True, 잘못되었으면 False를 출력하는 프로그램을
# 만들어라
#
# URL 규칙:
# http:// 또는 https://로 시작
# •도메인은 도메인.최상위도메인 형식이며 영문 대소문자, 숫자, -로 되어 있어야 함
# •도메인 이하 경로는 /로 구분하고, 영문 대소문자, 숫자, -, _, ., ?, =을 사용함
# 입출력 예시)
# 입력 - http://www.example.com/hello/world.do?key=python
# 출력 - True
# 입력 - https://example/hello/world.html
# 출력 - False

url=['http://www.example.com/hello/world.do?key=python','https://example/hello/world.html']
