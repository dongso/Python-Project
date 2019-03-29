#문자열 함수
x='hobby'
print(x.count('c'))
x='Python is the best language'
print(x.find('a')) #'a'가 처음 발견된 index를 반환
print(x.find('z')) #찾는 문자가 없을 때 return -1
print(x.index('a')) #검색 실패시 ERROR발생

#문자열 삽입(join함수)
print("#".join('abc'))  #결과 --> a#b#c
print(",".join(['a','b','c'])) #리스트 : [x1,x2,...,xn]

x='HELlo'
print(x.upper()) #upper(), lower()
print(x.lower())

#공백제거
x3="   hi   hello   "
print(x3.lstrip()) # 왼쪽부터 공백이 아닐때 까지 공백제거
print(x3.rstrip()) # 오른쪽 공백제거
print(x3.strip()) # 양쪽 공백제거

x4="Life is too short"
print(x4.replace("Life", "Your leg")) #Life를 Your leg로 대체해라
print(x4.split()) #공백으로 분리 후 List로 반환

#Split
x5="a$b$c$d::e$f"
print(x5.split('e'))

hnum=[1,3,5,7,9] #list_name=[x1, x2, ..., xn]
p=['john',20,190,True]
k=[1,2,['john',20,190,True]]
print(len(k))  #k의 사이즈=3 (요소의 개수)

#비어있는 리스트를 생성
x=list()
print(x) # []이 출력됨
x=[10,20,30,['a','b',['c',2]]]
print(x[3][:2])
# print(x[3][1]) #x[3]=['a','b','c'] ==> x[3][1] : b
# print(x[3][2][1])
# print(x[1:])

# x=[10,20,30]
# y=[40,50,60]
# print(x+y) #두 리스트가 연결됨
# print(x*3) #x의 값이 3번 나타남(반복)
#
# print(str(x[1])+"hello") #20hello
#
# y[1]=90

# del y[1]

#RANGE
a=list(range(10)) # 0~9
b=list(range(3,20)) # 3-19
a=list(range(-10,20))
a=list(range(-10,20,2)) #2씩 증가
a=list(range(100,20,-5))

print(a)

a.append([10,20])
print(a)
a.append(6000000)
print(a)
a=[10,40,20,30]
a.sort() # 오름차순으로 정렬
print(a)


a=['b','a','c','d']
#a.sort() # 오름차순으로 정렬
print(a)
a.reverse()
print(a)
a.insert(2,'k') #리스트 2번째 자리에 'k'추가
print(a)
a.remove('k')
print(a)
a.insert(2,'a')
print(a)
a.remove('a') #앞에 있는 a만 제거됨
print(a)

x=[10,20,30]
x.pop(0) #default::맨 마지막 index의 값이 pop됨// pop(index) 해당 index에 위치한 값이 pop()
x.append([50,100])

x=[10,20,30]
x.extend([50,100]) #요소로 추가
print(x)

x+=[200,300]
print(x)

a=(5,3,7,9)
a=5,3,7,9 #소괄호 없어도 tuple로 인식, but 소괄호 붙여서 표현하기
p=('john',25,180.0, True)

x=tuple(range(10,50,5))

x=[1,2,3]
x=tuple(x)

x=list('hello')
print(x)

y=tuple('hello')
print(y)


x=(1,2,3)
x=list(x)
x[1]=20
x=tuple(x)

x=(1,2,'a','b')
print(x[1:])
y=(100,200)
print(x+y)
print(len(x+y))













