print("만나서 반가워")

kor=100 #kor변수(기억장소)에 100을 저장해라
eng=90
mat=80

a=3.14
b=314e-2 #314 * 10^-2 (e: exponant)
c=3.14e2 #output: 314.0

#    변수 = 상수/변수/수식
#    d=c, d=c+1 가능!

print(a)
print(b)
print(c)

a=3
b=4
print(a+b, a-b, a*b, a/b, a%b,a**b,a//b)

msg = "Python\'s favorite language"
print(msg)

msg2= 'Python "favorite" language'
print(msg2)

msg3="python'fovorite' language"
print(msg3)

#여러줄에 걸쳐서 선언된 값을 가져오고 싶을때
alpha="a b c d e f g"
print(alpha)
alpha ="a b c d" \
       " e f g"
print(alpha) #위와 같은 값이 출력됨(한줄로)

alpha2="a b c d\n e\n f g"
print(alpha2)

alpha3=""" #위와 같은 값이 출려됨(여러줄로)
a b c d
 e
 f g
 """

print(alpha3)

a="Hi"
b="Tail"

print(a+" "+b)

print(a*3) #a가 3번 나옴
print(len("안녕 반가워"))

str="hello hi"
print(str[3]) #음수도 가능 print(str[-1])를 하면 i가 출력됨

print(str[2]+str[-1])
print(str[0:3]) #0부터 (3)-1까지

#ello 출력하기
print(str[1:5])

print(str[3:]) #3부터 끝까지 나옴
print(str[:3]) #앞에서부터 (3)-1까지 나옴
print(str[1:-3])

d = "20190328Sunny"
date = d[:8]
weather = d[8:]

print("date is ", date, " & weather is", weather)

x="hillo"
print(x[1])

x=x[0]+"e"+x[2:] #slicing 한 후에 오탈자 고치기
print(x)