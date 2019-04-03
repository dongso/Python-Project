#Debug 연습
# a=[]
# #line=[] #[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# for i in range(3):
#     line = []
#     for j in range(2):
#         line.append(0)
#     a.append(line)
#     print(a) #[[0, 0]]
#     print("="*50)
# print(a)
#파일 입출력
#f=open('test.txt', 'w') #open 후엔 close 꼭하기!! , mode::r,w,a(append)
#w모드일때 파일이 없으면 새로 만들어짐
#상대주소 :: 현재 프로젝트의 위치가 base 주소가 됨)
#f.close()

#f=open('d://test2.txt', 'w') #절대주소
#f.close()

# f=open("d:/file/myfile.txt",'w') #주의!!::기존에 있던 파일이름이랑 같으면 overwrite가 되버림
# for i in range(1,11):
#     data='%d번째 줄입니다.\n'%i
#     f.write(data) #file에 output 저장.
# f.close()
#
# #파일에 있는 내용 콘솔에서 출력
# f=open("d:/file/myfile.txt",'r')
#
# while True:
#     line=f.readline()
#     if not line: break #line에 저장된 것이 없으면.
#     print(line)
#
# f.close()

#readlines()::모든 줄을 읽어서 리스트 형태로 Return.
#read():: file 전체의 내용을 문자열로 Return
#readline():: 한줄씩 읽어서 문자열로 Return

# f=open("d://file/myfile.txt","a")
# for i in range(11,20):
#     data="%d번째 줄입니다.\n"%i
#     f.write(data)
#
# f.close()

# with open("foo.txt",'w') as f: #file close() 안해도됨.
#     f.write("Life is too short!\n")

print(round(1.123456,3)) #round(n, i)::i+1자리에서 반올림을 하는 함수

#sort() & sorted()
x=[5,3,1,4]
x.sort() #x.sort() // x자체가 정렬이 됨.
#y=x.sort() #정렬된 x객체를 y에 저장.
print(x)
#print(y)

x=['k','y','a','Z','ab']
x=sorted(x)
print(x)

print(str(3))
print(sum([1,2,3,4,4,5])) #sum의 인자로는 iterable한 데이터가 들어가야된다.(list/tuple)
print(list(zip([1,2],[5,6],[4,8]))) #zip::리스트 내에 튜플로 동일한 인덱스 위치의 데이터가 묶여서 저장.
print(list(zip("abcefg","def"))) #개수가 다르면 같은 부분까지만 zip

msg="hello world"
print(msg.replace('world','python'))
print(msg) #msg값이 변하지는 않는다.
msg=msg.replace('world','python') #저장하고 싶으면 assign 할것!
print(msg)

#문자 변경시에는 maketrans
#make transrate::문자 변경 규칙 생성
#str변수.maketrans()
myrule=str.maketrans('aeiou','12345')
print('apple'.translate(myrule))
print(msg.translate(myrule))

fruits=['apple','grape','orange']
print('-'.join(fruits))
myStr=' '.join(fruits) #공백으로 join
print(myStr.split(' ')) #공백으로 split

myStr=",.,.,., python.,.,.,.,. "
print(myStr.lstrip(',. '))
print(myStr.rstrip('., '))

import string
print(string.punctuation)

myStr=",.,.,.,^#@$!@# python.,.,.,.,.^#@$!@# "
print(myStr.strip(string.punctuation+' '))

myStr = "python"
print(myStr.rjust(10)) #10자리 확보 후 우측정렬
print(myStr.ljust(10)) #10자리 확보 후 좌측정렬
print(myStr.center(10)) #10자리 확보 후 가운데 정렬

myStr="apple plineapple"
print(myStr.find('a')) #1
print(myStr.find('pl')) #2 //apple에서 index 2부터 pl이 시작하기 때문에 2가 return 됨.
print(myStr.find('pa')) #없기 때문에 -1
print(myStr.count('pl'))
print(myStr.rfind('pl'))
print(myStr.find('pl')) #3개이상 있을 때 가운데 끼어있는 문자열의 경우 검색 불가.

import pickle
# 객체 단위로 저장 및 불러오기를 할 수 있는 모듈
# 객체::클래스로부터 파생된 실체
# ex. 붕어빵 : 붕어빵기계로부터 구어진 빵
# => pickle:: 붕어빵을 저장하겟따.
# 텍스트 파일 저장: 1번째 줄입니다\n
# 객체 저장 : {width:10, height:5, cont:'팥'...} //딕셔너리 형태

import pickle
f=open('myPickle.txt','wb') #write binary ::"객체를 저장하겠다(2진수)"
data={1:'python',2:'java'}
pickle.dump(data,f) #binary file로 저장됨
f.close()

f=open('myPickle.txt','rb') #read binary
data=pickle.load(f) #binary file을 load해서 data에 저장.
print(data)
f.close()

import shutil
shutil.copy('myPickle.txt','myPickle2.txt') #file copy

x={'a':10,'b':20,'c':30,'d':40}
x.setdefault('e')
x.update(a=90) #a의 값을 90으로 update
x.update(e=50)
x.update(a=900,f=90) #key가 있으면 value update, 없으면 추가
print(x)

y={1:'one',2:'two'}
y.update({1:'ONE',3:'THREE'})
y.update([[1,'ONE'],[3,'THREE']]) #list를 인자로 가질수도  있다. //위의 표현받식과 같은 결과를 갖게됨.
print(y)

x={'a':10,'b':20,'c':30,'d':40}
ret=x.pop('a') #pop을 하면서 value가 return 됨.
del x['d']
x.clear() #x에 저장된 모든 값 삭제

#문제
x={'a':10,'b':20,'c':30,'d':40}
#for, 딕셔너리 데이터 출력

for k,v in x.items(): #(key, value) 형태로 가져오기때문에 k,v
    print(k,v)

#딕셔너리의 key들만 출력 (a b c d...)
for k in x.keys():
    print(k,end=' ')





























