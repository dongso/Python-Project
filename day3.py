#Dictionary :: Key(변하지 않는 값)와 Value(변하는/변하지 않는 값)의 쌍으로 데이터를 표현하는 자료구조
#DictionaryName={Key:Value, ...}
#score={'kor':90}  => Key : 'kor', Value=90
#'key'::''를 사용해 key임을 나타내준다(문자열) , ''를 쓰지 않으면 변수.
#key-value의 대응은 1:1
score={'kor':90, 'eng':90, 'mat':70, 'kor':100}

a={1:'hi'} #key:1, value:'hi'
a={1:'hi', True:'hello'} # 1과 True가 중복!
a={1:'hi', False: 'hello'} # key:False, Value:'hello', 실제로 이런식으로 안씀
a={1:'hi', False: 'hello', 3.14:[1.5,2.5]} # Key에는 숫자, boolean 모두 올 수 있다.

#b= {[1,2]:100} # unhashable type::키에는 list가 올 수 없다.
#c={{'a':1}:200} # unhashable type::Key에 Dictionary가 올 수 없다.

#<<--딕셔너리 만드는 방법 -->>
x=dict() # 비어있는 딕셔너리가 생성됨.
x2={} # 비어있는 딕셔너리가 생성됨.
a={1:'hi'} #key:1, value:'hi'
x3=dict(kor= 90, eng=70) #key를 홀따움표 없이 작성
x4=dict(zip(['kor','eng'],[90,80]),spn=100) # zip([Key1, Key2,..], [Value1, Value2,...])
x5=dict([('kor',90),('eng',80)]) #dict에 대한 인수로 list를 보낼 수 있음. / 리스트의 인자로 튜플일 수도 있음.
# 요소 값이 2개인 튜플 2개가 리스트로 저장되어 dict함수에 인수로 전달됨.
score2=dict({'kor':90, 'eng':90, 'mat':70, 'kor':100})

a={1:'x'}
a[2]='y' # Dictionary a에 2라는 키에 해당하는 값으로 y를 삽입
a['name']='kim'
print(a[1]) #Dictionary a의 key 1에 대한 값을 출력
#print(a[0]) #Error:: key:0 없음
print(a['name']) #당연히 출력됨.
a['name']='park' #기존에 있던 'name'의 값을 'kim'->'park'으로 변경, name이라는 키가 없으면 추가, 있었으면 변경
#키에는 3, 값으로는 'z'로 하여 a 딕셔너리에 데이터를 추가하시오.
a[3]='z'

#del : 특정 키와 값을 삭제하고자 하는 경우
del a[1]
#a.pop('name')

#키 in 딕셔너리
print(1 in a) #a안에 1이라는 키가 있나? => 예/아니오.
print('nickname' not in a) #a안에 3이 없나? => 예/아니오
len(a) #Dictionary a에 몇개의 쌍이 존재하는가를 return

job={'손흥민':['축구','인공지능']} # 값이 여러개인 경우에는 list나 tuple을 사용함.
a.keys() #a 딕셔너리에 어떤 키들이 있는지를 확인하고 싶을 때
list(a.keys()) #a 딕셔너리에 어떤 키들이 있는지를 확인하고 싶을 때 출력 결과를 list로 표현하는 방법

print("*"*100)
for x in a.keys(): #특정 문장을 반복할 떄 사용 [2, 3, 'name']
    print(x)

print(type(list(a.values())))
#print(a.items()[0]) #TypeError: 'dict_items' object does not support indexing
print(list(a.items())[0]) #list로 변환하면 indexing 사용가능
print(list(a.items())[0][1]) #(2,'y')에서 1번째 위치에 y

a={'x':20, 'y':50, 'sum':70}
print(a.get('x'))
sum=a.get('x')+a.get('y')
print(sum,a.get('sum'))
print('sum' in a)

student={'cp':114,'addr':{'seoul':'hwagok','jeju':'jejusi'}} #dictionary안에 dictionary가 올수있다.(중첩 딕셔너리구조)
#중첩은 메모리가 허용되는 범위까지 무한으로 중첩할 수 있음.(하지만, 너무 많이 중첩하면 가독성이 떨어짐)

#SET : 1)중복을 허용하지 않는다. 2)순서가 없다.
s1=set([1,2,3,3]) #중복된 데이터는 제거. 리스트를 집합으로 변환
s2=set('hello') #'hello'를 문자 하나씩 쪼개서 set에 저장됨(중복된 문자는 제거됨)

s1=set([1,2,3])
s2=set([3,4,5])
#교집합
print(s1&s2)
print(s1.intersection(s2)) # == s2.intersection(s1)

#합집합
print(s1|s2)
print(s1.union(s2)) # == s2.union(s1)

#차집합
print(s1-s2)
print(s1.difference(s2))

s1.add(4)
print(s1)
# 두 개 이상 데이터는 동시 추가 불가
#s1.add(5,6) #Error :: add() takes exactly one argument
#s1.add([5,6]) #Error :: unhashable type:'list'
#s1.add({5,6}) #Error :: unhashable type: 'set'

#두개 이상 데이터 삽입 방법
s1.update([5,6])
print(s1)

s1.remove(4)

#반복문
a=[1,3,2]
print(a.pop()) #list(순서가 존재)의 가장 마지막 데이터를 삭제
print(a.pop())
print(a.pop())
print(a)

#While
a=[1,3,2]
while a: #a에 자료가 있는 동안 아래 코드를 수행
    print(a.pop())

if [] : #if 조건문 // 조건문자리에 리스트를 쓸 수 있음. , empty list => False
    print("데이터가 있습니다.")
else :
    print("데이터가 없습니다.")

x=[1,2,3,4]
if x : #현재 리스트 x가 비어있지 않으므로 "데이터가 있습니다."가 출력됨.
    print("데이터가 있습니다.")
else :
    print("데이터가 없습니다.")

if "" : #문자열 :: "" || ''일때만 거짓
    print("데이터가 있습니다.")
else :
    print("데이터가 없습니다.")

if 0 : #0일때만 거짓, -1도 참.
    print("데이터가 있습니다.")
else :
    print("데이터가 없습니다.")








