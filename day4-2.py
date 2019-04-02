def addMany(cal,*var): #pointer

    if cal=="add":
        res = 0
        for v in var:
            res=res+v
    elif cal=="mul":
        res=1
        for v in var:
            res=res*v

    return res
# print(addMany("add",1,3,5))
# print()
# print(addMany("mul",1,3,5,7,9))


def am(a,b):
    return a+b, a*b

res=am(3,4)
#print(res) #결과가 튜플 형태로 저장됨. (a+b, a*b)

def sayNick(n):
    if n=="바보" :
        return
    print("내 별명은 %s입니다." %n)

sayNick("바보")


def say3(name, old, man=True): #man=Ture, 초기값이 부여된 함수
    print("My name is %s"%name)
    print("age is %d"%old)
    if man:
        print("남")
    else:
        print("여")
say3("홍길동",20) #인수의 개수가 맞지 않아도 man에 default값이 지정되어있기 때문에 괜찮다!
say3("홍길순",18, False) #man의 값이 false로 update


#함수 내부에서 외부에 있는 변수를 변경
print("*"* 50)
a=1
def vtest(a):
    a=a+1
    return a

res=vtest(a)
print(res)

a=1
def varTest():
    global a #함수 내부에서 외부에 있는 변수를 사용 a가 전역변수임을 나타냄
    a=a+1
varTest()
print(a)


##Lambda function Definition
add=lambda a,b:a+b #add::rambda function
res=add(3,4)
print(res)
#->
#def구문으로 변경
def add(a,b):
    res=a+b
    return res
print(add(3,4))

add=lambda a,b=1:a+b #default값 정의 가능
#print(add(5))


#filter 함수
res=[]
def pos(x):
    if a in x:
        if a > 0:
            res.append(True)
        else:
            res.append(False)
    return res

print(pos([1,-3,2]))

print("*"*50)
def pos2(x):
    return x > 0
print(list(filter(pos2,[1,-3,2]))) #filter함수::함수 호출 후 리턴된 값이 true인 것만 묶어주는 역할

print(list(filter(lambda x:x>0,[1,-3,-6,6]))) #anomynous funciton(익명함수)
#filter(function,iterable)

print(hex(20)) #0x14 //16진수 14입니다.
print(int('11',16)) #16진수: 11 --> 10진수: 17
print(int('A',16)) #16진수: A --> 10진수: 10
print(int('101',2)) #2진수: 101 --> 10진수: 5

print(len('python'))
print(len([1,2,3,4]))
print(len((1,'a')))

#map(function, data) : 특정 자료에 대해 특정 함수를 적용
def threeTimes(num): #수치 데이터를 전달받아 3배를 한 값을 리턴
    res=[]
    for x in num:
        res.append(x*3)
    return res

print(threeTimes([1,2,3,4]))
# --> MAP FUNCTION
def three_times(num):
    return num*3
print(list(map(three_times,[1,2,3,4])))
print(list(map(lambda num:num*3, [1,2,3,4])))

















