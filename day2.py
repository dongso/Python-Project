# a=1
# if a==1: #a의 값이 1이라면
#     print("a is 1") #tab으로 종속관계 나타냄!!
# print("이 문장은 조건문과 관계가 없습니다")
#
# print(5//2) #몫: //  정수끼리 연산 ==> 결과 : 정수
# print(5//2.0) #정수와 실수를 연산 혹은 실수와 정수를 연산 ==> 결과 : 실수
# print(5.0//2)
# print(5.0//2.0) #실수끼리 연산 ==> 결과 : 실수
#
# print(int(3.14)) #3.14를 int함수의 인자로 넘겨주면 int형으로 반환
# print(int(5/2))
#
# print(int('5')+1) #문자 5를 int로 형변환 후 1과 덧셈
#         #str+int => ERROR
#
# print('5'+str(1))
#
# print(type('5'+'1'))
# print(type(int('5')+1))
# print(divmod(6,4)) #divmod(a, b) => 결과 : (몫, 나머지)
# q, r=divmod(6, 4) #결과값이 알아서 q와 r에 assign됨
# print(q,r)
#
# a, b=100, 200 #변수명1, 변수명2,... = 값1, 값2,... //이렇게 값 할당해도 됨!!
#
# print(float(5)) #정수5를 실수5.0으로 캐스팅
# print(float(5/2))
# print(float('50'))
# print(float('5.5')+1) # ('5.5'->5.5) + (1-> 1.0) = 6.5
#
# a=c=b=5 #한번에 값저장 [1) b=5 2) c=b 3) a=c] 차례로 수행됨.
#
# #How to swap x and y
# #1번
# x=2; y=5
# temp=x;
# x=y
# y=temp
#
# #2번
# x = 2; y = 5
# x, y = y, x #동시에 이뤄지기 때문에 temp를 안써도 swap을 할 수 있음.
#
# del x #x변수 제거(메모리에서 할당 해제)
# x=None #x변수 선언(변수에 값이 없는 상태)
# x=5 #여기서 값을 저장한거다~~
#
# y=1
# y+=2 #y=y+2 더하기 자리에 다른 연산자들 모두 가능
# print(y)
# a=5
# a=-a #부호 바뀜
#
# msg=input("문자열을 입력해 주세요 : ") # keyboard input을 받은 값을 msg에 할당
# print("입력한 문자열은 "+msg)
#
# x=input("첫번째 숫자 입력 : ") #input으로 받으면 문자열로 받게됨
# y=input("두번째 숫자 입력 : ")
# #print(int(x)+int(y))
#
# #x=int(input("숫자로 입렫됩니당^^ : "))
# #print(type(x))
#
# # x,y=input("두개를 입력하세요 : ").split() # 공백을 기준으로 값을 나눔
# # print(x,y)
#
# # x,y,z=input("두개를 입력하세요 : ").split() # split() :: 공백을 기준으로 값을 나눔
# # print(x,y,z)
# #
# # x,y,z=input("두개를 입력하세요 : ").split(',') # split() :: ,를 기준으로 값을 나눔
# # print(x,y,z)
#
# map(적용하려는 함수, 적용시키려는 값)
# a,b = map(int, input('숫자 두개 입력하세요').split()) # int형식으로 입력을 받음
# print(a+b)
#
# print(2>5)
# print("hi"=="hi") # 두 문자열이 같은가? 예(True)
# print("hi"!="hi") # 두 문자열이 같지 않은가? 아니오(False)
# print("hi" != "Hi")
print("="*50)
print(True and False) #and(&), or(|) : 논리 연산자
print(1>3 or 1<3)
#not : 논리값을 반대로
print(not True)
# 논리 연산자 우선순위 : not > and > or
print(not True and False or not False)
#False and False or not False
#False and False or True
#False or True
#True

print(bool(1)) # bool : 정수, 실수, 문자열을 논리값(bool 자료형)으로 변환

hi=''
if bool(hi) :
    print("hahaha")

#문자열 formatting
print("I eat 5 cookies.")
print("I eat %d cookies."%8) #%d : 포맷코드
a=10
print("I eat %d cookies."%a)
num=100
day=2
print("\n\n\n\nI eat %d cookies.\n\nI was sick %s days/ %.2f%%"%(num,day,day/365*100))

msg='Python\'s favorite hobby is football'
print(msg)
msg2="\"Python is very easy.\", he said."
msg2='"Python is very easy.", he said'
print(msg2)

print("%-10s John" %("hello")) # %Ns //N칸을 확보한 이후 N>0::우측정렬 s출력, N<0:: 좌측정렬 s출력

print("%10d"%1000)
print("%10d"%100)
print("%10d"%100000)

print("%f" %(3.141592789)) #소수이하 6번째 자리 수 까지 표현됨(7번째 자리에서 반올림)
print("%.8f원주율" %(3.141592789)) #소수점 이하 8번째 자리 수 까지 표현
print("%-20.8f원주율" %(3.141592789)) #20자리를 확보한 후 , 소수점 이하 8번째 자리 수 까지 표현

#format: 문자열의 형식 지정 함수
print("="*100)
print("I eat %d apples." %(6))
print("I eat {} apples.".format(5)) #m: method
print("I eat {0} apples.".format(5)) #{n}:: format함수의 n번째 인수
print("I eat {1} apples.{0}".format(5,1,2))
print("I eat {1} apples.{0}".format(5,"three"))

num=5
day="four"
print("...{n}  {d}".format(n=10, d="two")) #인자에 이름을 정해서 이름으로 값을 전달 할 수도 있다


cha="...{n}...{d}".format(n=154, d="two")
print(cha)
#:>n 는 우측정렬, n자리수
print("{0:>10}".format("hello"))
print("{0:<10}".format("hello"))
print("{0:^10}".format("hello"))
print("{0:=^10}".format("hello")) #가운데정렬을 하고 나머지 공간을 '='로 채워라(다른문자도 가능)

print("{{ and }}".format()) #{ and }를 출력하고 싶다.

#내 이름은 상공입니다. 나이는 25입니다. 출력하기
name="상공"
age=25
print("내 이름은 {0}입니다. 나이는 {1}입니다.".format(name,age))
print("내 이름은 %s 입니다. 나이는 %d입니다."%(name,age))
print("내 이름은 {name}입니다. 나이는 {age}입니다.".format(name="상공",age="26"))













