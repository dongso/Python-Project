rating={
    '홍길동':{
        '밀정' : 4,
        '암살' : 3    },
    '임꺽정':{
        '밀정' : 4,
        '암살' : 3    }
}
#print(rating['홍길동']['암살'])
rc=rating
# print(rc)
# print(rc['홍길동']['밀정'])
rc['홍길동']['밀정']=5 #rating에 저장된 ['홍길동']['밀정']의 값까지 변경됨.
# print(rc)
# print(rating)
# print(rc is rating)

plus_ten=lambda x:x+10
def plus_ten2(x):
    return x+10
#
# print(plus_ten(1))
# #print(list(map(plus_ten,[1]))[0])
# print(list(map(plus_ten,[1,2,3])))
# print(list(map(lambda x:x+10,[1])))

#lambda 매개변수: 식1 if 조건식 else 식2
#식1: IF조건을 만족했을 때, 식2: if조건 만족하지 못했을 때
#lambda에서는 elif를 못쓴다.


#3의 배수는 해당 수를 문자로 변경하시오.
#[1, 2, '3', 4, 5, '6', 7, 8, '9', 10]
a=list(range(1,11))
print(list(map(lambda x: str(x) if x%3==0 else x,a)))

#lambda에서 다중조건 사용하기
#lambda 매개변수들 : 식1 if 조건식1 else 식2 if 조건식2 else 식3

#x가 1이면 '1', 2이면 2.0으로 변경, 나머지는 10을 더해서 출력
# ['1', 2.0, 13, 14, 15, 16, 17, 18, 19, 20]
a=list(range(1,11))
print(list(map(lambda x: str(x) if x==1 else float(x) if x==2 else x+10 , a)))

def func(x):
    if x==1: return str(x)
    elif x==2: return float(x)
    else: return x+10

print(list(map(func,a)))  #map(적용할 함수,literable data)

#원하는 결과 : a,b요소간의 곱셈
#[2,8,18,32,50]
a=[1,2,3,4,5]
b=[2,4,6,8,10]
print(list(map(lambda x,y:x*y , a,b )))

def f(x):
    return x>5 and x<10
a=[8,3,1,9,10,6]
print(list(filter(f,a)))

x=10 #전역변수 : 전체에서 접근 가능.

def foo():
    print(x)

foo()
print("x"*100)

def foo2():
    x2=100 #지역변수 : 한정된 범위 안에서만 사용가능한 변수
    print(x2)


print("x"*100)
x3=50
def foo3():
    x3=100 #foo3안에 지역변수로 새로 x3을 선언해서 사용하는 것임.
    print("in the foo3",x3)
foo3()
print(x3) #전역변수 x3을 출력해라~~

#함수 내부에서 전역 변수의 값을 변경하고자 하면 =-> global 키워드를 사용하면 됨.

def foo4():
    global  x3 #global변수로 먼저 선언,
    x3=100     #원하는 값 대입
    print(x3)

print("x"*100)
foo4()
print(x3)

#전역변수가 없는 상태에서 함수 내부에서 global을 사용하면 -> 해당 변수는 전역변수가 된다.
def foo5():
    global xxx #xxx를 전역변수로 사용하겠다.
    xxx=20
    print(xxx)

foo5()
print(xxx) #전역에 'xxx'변수를 선언하지 않아도,
            #foo5()에서 'xxx'를 global로 선언했기 때문에
            #전역변수로 사용가능하다.

#######################################연습문제############################################
#filter, lambda
#x=[1,-2,3,-4,5,-7,-9] 리스트에 음수를 제거하고 출력해라

x=[1,-2,3,-4,5,-7,-9 ]
print(list(filter(lambda a:a>0, x)))
# def a(a):
#     return a>0 // 위의 lambda함수와 같은 동작을 함.







