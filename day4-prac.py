#문제 1
print("문제 1번 ******************")
for i in range(1,6):
    for j in range(0,i):
        print(" ",end='')
    print("*\n")

#문제 2
print("문제 2번 ******************")
for i in range(2,10) :
    print("%i단 시작 -->"%i)
    for j in range(1,10):
        print("%s * %s = %d"%(i,j,i*j))

#문제 3
print("문제 3번 ******************")
def is_odd(num):
    res=""
    if num%2==0: res="짝수입니다."
    else: res="홀수입니다."
    return res
print(is_odd(1))

#문제4
print("문제 4번 ******************")
sum=0
cnt=0
while True:
    a=int(input())
    if a==0: break
    sum=sum+a
    cnt=cnt+1
print(sum/cnt)

#문제5
print("문제 5번 ******************")
numbers=[1,2,3,4,5]
result=[n*2 for n in numbers if n%2 == 0]
print(result)

#문제6
print("문제 6번 ******************")

def traf(age,balance):
    fare=0
    if age>=7 and age<=12:
       fare=650
    elif age>=13 and age<=18:
        fare=1050
    elif age>=19:
        fare=1250
    else:
        fare=0
    return balance-fare

age=int(input("당신의 나이는? "))
print(traf(age,9000))

#문제7
print("문제 7번 ******************")
start,stop=map(int,input().split())

def not_three(start, stop):
    for i in range(start,stop+1):
        if str(i)[len(str(i))-1]=='3':
            continue
        else:
            print(i,end=' ')

not_three(start,stop)

#추가문제
def count7(start,end):
    cnt=0
    for i in range(start,end+1):
        for j in range(0,len(str(i))):
            if str(i)[j]=='7':
                cnt=cnt+1
    return cnt
print(count7(1,10000))