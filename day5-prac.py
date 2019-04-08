#문제1
print("###1번문제###")
with open('d:/file/words.txt','r') as f:
    while True:
        line=f.readline()
        if not line: break #line에 저장된 것이 없으면.
        line=line[0:-1] #\n제거
        tf=True
        for i in range(0,int(len(line)/2)) : #반까지만 돌리면 됨.
            if line[i] != line[(-1)-i] :
                tf=False
                break
        if tf:
            print(line)

#문제2

def DicRemove(x):
    keyList=['delta']
    for k,v in x.items():
        if v==30:
            keyList.append(k)

    for i in keyList:
        x.pop(i)
    print(x)

for i in range(2):
    keys = input().split()
    values = map(int, input().split())
    x = dict(zip(keys, values))
    DicRemove(x)

#문제3

def find3N5():
    global num
    num=[]
    for i in range(1,1000):
        if i%3==0:
            num.append(i)
        elif i%5==0:
            num.append(i)
    sum=0
    for i in range(0,len(num)-1):
        if num[i] != num[i+1]:
            sum+=num[i]
    if num[-1] != num[-2]: sum+=num[-1] #마지막 경우 확인
    return sum

print(find3N5())
#문제4
a=[1,2,3,4]
print(list(map(lambda x:x*3,a)))
#문제5

def findMaxMin(a):
    min = 100
    max = -100
    for i in a:
        if i<min : min=i
        elif i>max : max=i
    print("최솟값 : %d, 최대값 : %d"%(min,max))

a=[-8, 2, 7, 5, -3, 5, 0, 1]
findMaxMin(a)

#문제6
with open('abc.txt','r') as f:
    global contents
    contents=[]
    while True:
        line=f.readline()
        if not line: break #line에 저장된 것이 없으면.
        contents.append(line)

with open("res.txt",'w') as f:
    for i in range(len(contents)-1,-1,-1):
        data=contents[i]
        f.write(data)

#문제 7
def replaceJava2Python():
    txt=[]
    with open("test.txt",'r') as f:
        while True:
            line=f.readline()
            if not line: break
            txt.append(line)

    with open("test.txt",'w') as f:
        for i in txt:
            if i.find('java') :
                i=i.replace('java','python')
            f.write(i)

replaceJava2Python()
#문제8

with open("sample.txt",'r') as f:
    cnt=0; sum=0
    while True:
        line=f.readline()
        if not line: break
        cnt+=1;
        sum+=int(line)

    with open("result.txt",'w') as writeFile:
        writeFile.write(str(sum/cnt))


#문제9\
tile=[]
copytile=[]

def tileCopy():
    global tile
    tile=copytile
    return
def reAlloc(i,j,dir):
    if dir=="right":
       for x in range(i,-1,-1):
            copytile[x][j]=tile[x-1][j]; copytile[x][j+1]=tile[x-1][j+1]; copytile[x][j+2]=tile[x-1][j+2]
            copytile[0][j]=0; copytile[0][j+1]=0; copytile[0][j+2]=0
    else:
        if i==2 :
            copytile[i][j]=0; copytile[i+1][j]=tile[0][j]; copytile[i+2][j]=tile[1][j]
        elif i==1:
            copytile[i][j]=0; copytile[i+1][j]=0; copytile[i+2][j]=tile[0][j]
        else:
            copytile[i][j]=0; copytile[i+1][j]=0; copytile[i+2][j]=0

    tileCopy()  #변경된타일의 위치 재 저장
    return
def anyFUNG():
    con=False
    while not con:
        con=True
        for i in range(0,5):
            for j in range(0,3):
               if tile[i][j] != 0 and tile[i][j]==tile[i][j+1] and tile[i][j+1] == tile[i][j+2]:
                   reAlloc(i,j,"right")
                   con=False
               else: con=True

        for i in range(0,3):
            for j in range(0,5):
                if tile[i][j] != 0 and tile[i][j] == tile[i + 1][j] and tile[i + 1][j] == tile[i + 2][j]:
                    reAlloc(i, j, "down")
                    con=False
                else: con=True
        #3개이상 연속 타일 -> reAlloc(i,j) 호출
    return

for i in range(5): #5x5 matrix생성(애니펑 초기 타일 입력받음)
    subtile = []
    for j in range(5):
        data=int(input())
        subtile.append(data)
    tile.append(subtile)

copytile=tile #초기 타일 copy
anyFUNG()
print("게임결과")
for i in range(5):
    print(tile[i])