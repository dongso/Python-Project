i = 0
while True:
    print(i)
    i = i+1
    if i == 100:
        break

for i in range(10000):
    print(i)
    if i==100:
        break

# ****
# ****
# ****

for i in range(3):
    for j in range(4):
        print("*",end='')
    print("\n")

# *
# **
# ***
# ****

for i in range(1,5):
    for j in range(i):
        print("*",end='')
    print("\n")

a=[(1,2),(3,4),(5,6)]
for x in a:
    print(x)

a=[(1,2),(3,4),(5,6)]
for x in a:
    print(x[0]) #각 튜플의 0번 index의 값이 출력됨.

for x1, x2 in a:
    print(x1+x2) #튜플로 이뤄져있을때 알아서 첫번째, 두번째 값이 x1, x2로 불려짐.

#리스트 내포(list comprehension)::리스트 내부에 for문을 포함
a=[1,2,3]
res=[ n*2 for n in a] #a의 값을 2배한것을 res에 저장.

print(res)

a=[1,2,3,4,5,6]
#a리스트의 요소 중 2의 배수인 것만 2배 해서 res 리스트를 생성
res=[ n*2 for n in a if n%2 == 0] #a리스트의 요소 n이 만약에 2의 배수이면, n*2를 해서 res리스트에 저장.
print(res) #[4,8,12]
#구문형식 -> 리스트변수명 = [표현식 for 변수 in 리스트 if 조건문]

#다중 for문 가능.
res=[x*y for x in range(2,10)
     for y in range(1,10)]
print(res)

#2차원 리스트 :: 리스트 안에 리스트가 들어가있는 구조
a=[[1,2],[3,4],[5,6]]
print(a[2][1]) #세로 index:2, 가로 index:1

print("*"*50)
a=[[1,2],[3,4],[5,6]]

for k in range(len(a)):
    for j in range(len(a[k])):
        print(a[k][j],end=' ')
    print()

i=0
print("*"*50)
a=[[1,2],[3,4],[5,6]]

while i<len(a): #3번 반복
    j=0
    while j<len(a[i]):
        print(a[i][j],end=' ')
        j=j+1
    i=i+1
print("*"*50)

a = []
line=[]
for i in range(3):
   # line=[] #line 초기화
    for j in range(2):
        line.append(0)
    a.append(line)

########내 장 함 수 ##########
print(abs(-3)) #절대값
print(abs(-3.1))
print(all([1,2,3,0])) #all함수는 모든 요소가 참인가? 참 : True, 거짓: False
print(any([0,0,0,1]))
print(chr(97)) #아스키 코드값->문자

for n in enumerate(['i','j','k']):
    print(n)
print(eval('1+2'))
print(eval('divmod(5,3)'))

########함수 정의 ########

def pos(x): #함수 정의 부분(단독으로 실행되지 않는다.-> 호출 필요!!)
    res=[] #x리스트에서 양수값만 뽑아서 res 리스트에 넣자
    for i in x:
        if i > 0 :
            res.append(i)

    #res=[i for i in x if i>0]
    print(res)

print("*"*100)
pos([1,-3,2]) #함수 실행부분

def 버스이용(): #함수정의
    print("버스를 탔어요")
버스이용() #함수 호출


def 버스이용2():  # 함수정의
    print("버스2를 탔어요")
버스이용2()  # 함수 호출

def 버스이용3(왼쪽주머니, 오른쪽주머니): #버스 요금 1500원
   잔액=왼쪽주머니-1500
   print("잔액 : ", 잔액)
   잔액=오른쪽주머니 -1500
   print("잔액 : ", 잔액)
   print("버스3을 타고 이동합니다.")


버스이용3(2000,10000)

def sub(inse):
    fee=1200
    rest=inse-fee
    return rest
print(sub(2000))

def add(a,b):
    return a+b
print(add(2,3))

def say():
    print("hi")
    return
res=say() #return value is None.
print(res)

def add2(a,b):
    return a+b
res=add2(b=3,a=5)
print(res)

def fact(val):
    res=1
    for v in range(1,val+1):
        res=res*v
        #print(v)
    return res
print(fact(5))


#1부터 data 변수로 전달된 값까지 존재하는 모든 4의 배수를 출력.
#예시: 값을 입력하세요:10
#4,8
def calc(data):
    for i in range(1,data+1):
        if i %4 == 0:
            print(i)

myInput=int(input("값을 입력하세요 : "))
res=calc(myInput)
print(res)