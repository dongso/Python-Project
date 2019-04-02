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