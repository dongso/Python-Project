# #정규표현식 : 패턴(규칙)을 가진 문자열을 표현하는 방법
# #규칙이 있는 문자열을 추출, 변경 등의 작업을 수행하기 위해 작성
# #re module을 사용해서 정규표현식 작성.
# #re.match('패턴','문자열')을 사용.
#
import re
print(re.match('Hi', 'Hello, hi, world'))
print(re.match('hi', 'hi, world')) #문자열의 첫번째부터 비교해서 있으면 span(0,n) return
print('hello hi, world'.find('hi')) #문자열의 시작위치가 나옴
# #re.match는 find()에서 찾을 수 없는 문자열도 찾아 낼 수 있다.
#
# #search 함수
# #^문자열 : 패턴이 문자열이 맨 앞에 오는 판단
# #문자열$ : 패턴이 문자열의 마지막에 오는지 판단
print(re.search('hi','hello, hi')) #문자열에 hi가 있는가? # hi의 위치를 span(i,j)로 return
print(re.search('^hi','hi hello')) #맨 앞에 hi가 있는가?
print(re.search('hi&','hi, hello')) #맨 뒤에 hi가 있는가? None

print("***********"*10+'\n',re.match('hello|world','hello world')) #주어진 문자열에 hello || world가 포함되어 있나?

# #문자열이 숫자로 되어 있는지 판단하기 위한 정규표현식의 예
# #대괄호 안에 숫자의 범위를 기재, * 또는 + 기호를 붙임
# #*:0개이상, +:1개이상 있는지 판다.
# print(re.match("[0-9]*","1234")) #1234에는 [0-9]* 패턴이 있나?
# # [0-9]* : 0부터 9까지의 숫자가 0개 이상 존재하는 패턴이 있나?
# # 있으면 return span(i,j):: i부터 j까지 매치됨
# #match는 문자열의 시작부터 확인함
# #따라서, re.match("[0-9]*, "문자열") :: 문자열이 숫자로 시작하는지를 확인하는 것.
print(re.match("[0-9]*","1234a"))
print(re.match("[0-9b-k]*","c1b123a")) #문자열에 0-9 & c, b가 있는지 확인

print("*"*50)
print(re.match("a*b","b"))
# #a*b의 의미 :: 문자열에 a가 0개이상 나온 뒤에 이어서 b가 있는 패턴이 존재하는가?
print(re.match("a+b","b"))
# #a+b의 의미 :: 문자열에 a가 1개이상 나온 뒤에 이어서 b가 있는 패턴이 존재하는가?
print(re.match("a+b","aaacb"))
print(re.match("a+b+","aabbaabb"))
print(re.match('sab+cc','sabee'))


# #? 와  .::문자가 한 개만 있는지 판단 할 때 사용
# #? : 문자가 0개 또는 한개
# #. : 문자가 1개인지 판단.
print(re.match('H?','H'))
print(re.match('H.','IW'))
print(re.match('H.',"HHHHHHHEL"))

print("*"*50)
# #문자가 정확히 몇 개 있는지 판단.
# #문자{개수}
# #(문자열){개수}
print(re.match('h{3}','hhello')) #h가 3개 있는지 판단 , 매치 안됨
print(re.match('h{4}','hhhhhello'))
print(re.match('h{4}k','hhhhkkkkhello'))
print(re.match('h{4}k+','hhhhkkkello'))
print(re.match('h{3}k*',"hhhello"))
print(re.match('h{3}k*hel{2}','hhhhello'))
print("*"*50)
print(re.match('(he){2}k+','hehekkk'))
print(re.match('(hi){3}','hihi'))
print(re.match('[0-9]*(hi){3}b*y*e','1hihihiyye'))
print(re.match('(hi){3}b*y*e','hihihiyy')) #None::"e"가 없기 때문에
print(re.match('(hi){3}[a-z]*e','hihihiydsfaasdfy'))
#
# #특정범위의 문자/숫자가 몇 개 있는지 판단 :: [범위]{개수}
print("*"*50)
print(re.match('[0-9]{4}','010-1234'))
# pNum=input("전화번호를 입력해주세요")
# print(re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}',pNum)) #전화번호 확인 할때 유용하게 사용됨.

print(re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}','010-1234-5678')) #전화번호 확인 할때 유용하게 사용됨.
print("*"*50)
print("*"*50)
# #범위지정
print(re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}', '02-123-4567')) #개수의 범위도 지정 가능.
print(re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}', '032-1234-5678'))
print(re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}', '02-13-4567')) #None

#
# #문자에 대한 개수 지정
print("="*100)
# # (문자){시작개수, 끝개수}
# # (문자열){시작개수, 끝개수}
# # [0-9]{시작개수, 끝개수}
print(re.match('(a){2,3}', 'a')) #None
print(re.match('(a){2,3}', 'aa'))
print(re.match('(a){2,3}', 'aaa'))
print(re.match('(a){2,3}', 'abaaa')) #None

print(re.match('(hi){2,3}', 'hihihihello')) #None
#
#
# print("="*100)
# #숫자와 영문을 혼합
# #0-9, a-z, A-Z
print(re.match('[0-9]+','1234'))
print(re.match('[0-9o]+','o1234')) #대괄호 안에서는 순서가 없다.
print(re.match('[a-z0-9]+','aw1adf234')) #a-z and 0-9
print(re.match('[ol0-9]+','lo1234'))
print(re.match('[0-9lo]+','ello1234')) #None

print(re.match('[A-Za-z0-9가-힣]+','helloHHI홍길동'))
#특정 문자 범위에 포함되지 않는지를 판단
# [^범위]*
# [^범위]+
print(re.match('[^A-Z]+','hello가나다ABC')) #A-Z가 아닌 모든 문자열이 매치됨

#^[범위]*
#^[범위]+
print(re.match('^[A-Z]+','HELLO가나다')) #A-Z로 시작하는 문자열
print(re.match('^[A-Z]*','hello')) #A-Z로 시작하는 문자열

print(re.match('[0-9]+','1234'))
print(re.search('[0-9]+$','hello1234')) #숫자로 끝나는 경우 search함수를 사용할 것!

#특수문자판단
print(re.match("\*+","1**2")) #패턴에서 특수문자는 얖에 \를 붙여야한다.
print(re.search("\*+","1 **2")) #search 함수 : 문자열의 전체에서 패턴을 찾아줌

print(re.search("[*]+","1 **2")) #search 함수 : 문자열의 전체에서 패턴을 찾아줌
print(re.search("[*0-9]+","1** 2"))
print(re.search("[*]+","1 **2 *")) #search 함수 : 문자열의 전체에서 패턴을 찾아줌

print(re.match("[$()a-z]+","$(lunch)"))

#축약형 : \d(decimal) <-> \D(not decimal), \w
print(re.match("\d+",'1234')) # \d : 숫자([0-9])
print(re.match("\D+",'1234')) # \D : [^0-9]와 같음
print(re.match("\D+",'abc1234')) # \D : ^[0-9]와 같음
print(re.match("\w+",'1234')) # \w : [a-zA-Z0-9 ]-=> 소문자,대문자,숫자,blank까지 포함
print(re.match('\W+','.?')) # \W : [^a-zA-z0-9 ]-=> 소문자,대문자, 숫자, 빈칸을 제외한 문자

print(re.match("\w+","abcd_1234"))
print(re.match("\W+","*^^* hello *^^*"))

print(re.match('[a-zA-Z0-9\s]+','Hello 1234')) #\s ::blank

#같은 정규표현식 패턴을 자주 사용해야 하는 경우에는
#매번 match, search를 사용해서 패턴을 지정하고 매칭 테스트하는건 비효율적이다.
#compile 함수 : 같은 패턴이 반복적으로 사용되는 경우에 적합
print("--------------------compile Example----------------------------")
pat=re.compile("[0-9]+") #정규표현식 패턴 정의 및 패턴 객체 생성
print(pat.match("1234")) #문자열 "1234"에 pat을 match해본다.
#print(re.match("[0-9]+","1234")
print(pat.search("1abcd"))


emailPat=re.compile("\w*\d*@\w+.\w+.*")
print(emailPat.match("khay0311@hufs.ac.kr"))