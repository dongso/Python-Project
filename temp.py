def count7(start,end):
    cnt=0
    for i in range(start,end+1):
        for j in range(0,len(str(i))):
            if str(i)[j]=='7':
                cnt=cnt+1
    return cnt
print(count7(1,10000))