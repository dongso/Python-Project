# if 개가 나타나면 :
#   차를 정지시킨다
# if 조건식 :
#   수행할 문장 //들여쓰기!!!
#   수행할 문장
#       .
#       .
#       .
# else : //위 조건문을 만족하지 못한 경우
#   수행할 문장 //들여쓰기!!!
#       .
#       .
#       .

x=10
if x==10 :
    print("x is 10")
else :
    print("x isn't 10")

if x==10 :
    pass        #pass:: C++의 continue와 같은 역할을 함
else :
    print("x != 10")

x=10
if x==10:
    print("x에는")
    print("10이 있어요")

# if 앞에 물체가 없음:
#     if 옆에서 뛰어들어오는 물체가 있음 :
#        자동차를 멈춘다
#

a=5
if a>=0 :
    print("a is over 0")
    if a==5:
        print("a is 5")
    if a==20:
        print("a is 20")

money=4000
card=True
if money>=5000 or card:
    print("택시타고간다.")
else :
    print("걸어간다.")

print('k' in 'korea') #'korea'문자열 안에 'k'문자가 있나?
if 'k' in 'korea':
    print('k가 있어요')
else :
    print("k가 없어요")

if 4 not in {1,2,3,4}:
    print("4 없음")
else :
    print ("4 있음")

x=1
if x==2:
    y=x
else :
    y=0

y=x if x==2 else 100 #축약형, 한줄로 줄여서 사용할 수 있음.

#score가 70이상이면 합격, 그렇지 않으면 불합격을 res 변수에 저장하는 구문을 "축약형"으로 작성해라

# score=int(input("점수를 입력해주세용 : "))
# res="합격" if score>=70 else "불합격"
# print(res)

if not 0: #not False(0) -> True
    print("0입니다.")
else:
    print("0이 아닙니다.")

if not None: #not False(None) -> True
    print("not None")
else :
    print("None")

sum=0; i=1
while i<=10 :
    sum=sum+i
    if i==10:
        print("모든 합을 구했습니다.")
        print("합 : ", sum)
    i+=1

num=1
pmt="""
1. add
2. del
3. list
4. quit
enter num? 
"""
# while num != 4 or (num>0 and num<4):
#     print(pmt)
#     num=int(input())
#
# while num>0 and num<4:
#     if num==4:
#         break
#     else:
#         print(pmt)
#         num=int(input())

#
# if 조건식:
#     코드1
# elif 조건식: //else if
#     코드2
# elif 조건식:
#     코드3
# else:
#     코드4

# button=int(input("원하는 음료의 번호를 입력해주세요. : "))
# if button==1:
#     print("콜라")
# elif button==2:
#     print("환타")
# elif button==3:
#     print("사이다")
# else:
#     print("메뉴없음")

# for i in range(10):
#     print("hello i : ", i)

# for i in range(0,10,2):
#     print("hello i : ", i)
#print("="*50)
# for i in range(10,0,-1):
#     print("hello i : ", i)

print("="*50)
for i in range(10,0): #default 증가 +1
    print("hello i : ", i)

str=('aa','bb','cc')
for s in str:
    print(s)

for letter in reversed('Python') : #반복문을 사용해서 문자를 출력해야됨. 그냥은 출력x
    print(letter, end='-') #option end =' ' //letter뒤에 넣을 문자

#print(reversed('Python'))

#1부터 100까지의 수 중에서 5의 배수를 제외한 나머지 수의 합을 출력

sum=0
for x in range(1, 101):
    if x % 5 != 0:
        sum += x
    else:
        continue

print('\n', sum)

a=0
while a<10:
    a=a+1
    if a % 2 == 0:  #짝수일때는 밑에 print(a)무시
        continue
    print(a) #홀수 값만 출력됨.

#함수 < 모듈(확장자 : .py)< 패키지

import random

print(random.random()) #Return the next random point number in the range[0.0, 1.0)
print(random.randint(1,46)) #정수 난수가 생성
print("-"*50)


#-----하영이의 로또 가게 -----#
li=set()
while len(li) < 6:
    r=random.randint(1,45)
    li.add(r)

print(li)
