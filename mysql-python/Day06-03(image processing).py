from tkinter import *
from tkinter.filedialog import *
import os.path
import math
from tkinter.simpledialog import *


## Define functions
def loadImage(fname):
#파일을 메모리로 로딩하는 함수
    global window, canvas, paper,inW, inH, outW, outH,inImage, outImage

#step1. 입력 이미지 초기화
    inImage=[]

#step2. 파일 크기 계산
    fsize=os.path.getsize(fname) #byte 단위
    inW=inH=int(math.sqrt(fsize))

#step3. 파일 크기 만큼 메모리 확보
    for i in range(0, inH):
        tmpList=[]
        for k in range(0, inW):
            tmpList.append(0)
        inImage.append(tmpList)

#step4. 파일-> 메모리로 옮기기
    fp=open(fname, 'rb')

    for i in range(inH):
        for k in range(inW):
            data=int(ord(fp.read(1))) #1개 픽셀 값을 읽음(0~255)
            inImage[i][k]=data

    fp.close()

def displayImage(image, scope=1):
    #image를 모니터에 출력
    global window, canvas, paper,inW, inH, outW, outH,inImage, outImage

    if canvas != None:
        canvas.destroy()

    window.geometry(str(int(outH*scope))+"x"+str(int(outW*scope)))
    canvas=Canvas(window, height=int(outH*scope), width=int(outW*scope))
    paper = PhotoImage(height=int(outH*scope), width=int(outW*scope))
    canvas.create_image((  int((outW*scope) / 2), int((outH*scope) / 2)), image=paper, state='normal')

#이미지 출력
    for i in range(int(outH*scope)):
        for k in range(int(outW*scope)):
            data=outImage[i][k]
            paper.put("#%02x%02x%02x" % (data,data,data),(k,i))
    canvas.pack()


def equalImage():
    #input Image == output Image
    global window, canvas, paper,inW, inH, outW, outH,inImage, outImage

#step1. 출력 이미지 초기화
    outImage=[]

#step2. outImage의 크기를 결정
    outH=inH; outW=inW

#step3. 파일 크기 만큼 메모리 확보
    for i in range(0, outH):
        tmpList=[]
        for k in range(0, outW):
            tmpList.append(0)
        outImage.append(tmpList)

#step4. 영상처리 알고리즘 구현 부분
    #여기서는 equal algorithm을 사용한다.

    for i in range(inH):
        for k in range(inW):
            outImage[i][k]=inImage[i][k]

    displayImage(outImage)

def openImage():
    #image 열기
    global window, canvas, paper,inW, inH, outW, outH,inImage, outImage
    filename = askopenfilename(parent=window, filetypes=(('RAW 파일','*.raw'),('모든 파일', '*.*')))

    if filename=="" or filename ==None :
        return
    print(filename)


    loadImage(filename)

    #inputImage -> outputImage
    equalImage()


def addImage():
    # output Image 밝게하기
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage

    # step1. 출력 이미지 초기화
    outImage = []

    # step2. outImage의 크기를 결정
    outH = inH;
    outW = inW

    # step3. 파일 크기 만큼 메모리 확보
    for i in range(0, outH):
        tmpList = []
        for k in range(0, outW):
            tmpList.append(0)
        outImage.append(tmpList)

    # step4. 영상처리 알고리즘 구현 부분
    # 여기서는 밝게한다.

    value=askinteger('밝게할 값', '값 입력 : ', minvalue=1, maxvalue=255)


    for i in range(inH):
        for k in range(inW):
            if inImage[i][k]+value>255: #overflow 해결방법
                outImage[i][k]=255
                continue
            outImage[i][k] = inImage[i][k]+value

    displayImage(outImage)

def subImage():
    #이미지 어둡게 하기
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage

    # step1. 출력 이미지 초기화
    outImage = []

    # step2. outImage의 크기를 결정
    outH = inH;
    outW = inW

    # step3. 파일 크기 만큼 메모리 확보
    for i in range(0, outH):
        tmpList = []
        for k in range(0, outW):
            tmpList.append(0)
        outImage.append(tmpList)

    # step4. 영상처리 알고리즘 구현 부분
    # 여기서는 어두워진다.

    value = askinteger('어둡게 할 값', '값 입력 : ', minvalue=1, maxvalue=255)

    for i in range(inH):
        for k in range(inW):
            if inImage[i][k] - value <0:  # overflow 해결방법
                outImage[i][k] = 0
                continue
            outImage[i][k] = inImage[i][k] - value

    displayImage(outImage)

def mulImage():
    #영상 곱셈
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage

    # step1. 출력 이미지 초기화
    outImage = []

    # step2. outImage의 크기를 결정
    outH = inH;
    outW = inW

    # step3. 파일 크기 만큼 메모리 확보
    for i in range(0, outH):
        tmpList = []
        for k in range(0, outW):
            tmpList.append(0)
        outImage.append(tmpList)

    # step4. 영상처리 알고리즘 구현 부분
    # 여기서는 밝게한다.

    value = askinteger('곱셈 할 값', '값 입력 : ', minvalue=1, maxvalue=255)

    for i in range(inH):
        for k in range(inW):
            if inImage[i][k] * value > 255:  # overflow 해결방법
                outImage[i][k] = 255
                continue
            outImage[i][k] = inImage[i][k] * value

    displayImage(outImage)


def divImage():
    #영상 나눗셈
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage

    # step1. 출력 이미지 초기화
    outImage = []

    # step2. outImage의 크기를 결정
    outH = inH;
    outW = inW

    # step3. 파일 크기 만큼 메모리 확보
    for i in range(0, outH):
        tmpList = []
        for k in range(0, outW):
            tmpList.append(0)
        outImage.append(tmpList)

    # step4. 영상처리 알고리즘 구현 부분
    # 여기서는 어두워진다.

    value = askinteger('곱셈 할 값', '값 입력 : ', minvalue=1, maxvalue=255)

    for i in range(inH):
        for k in range(inW):
            outImage[i][k] = int(inImage[i][k] / value)

    displayImage(outImage)


def reverseImage():
    #영상 반전 255->0. 254->1
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage

    # step1. 출력 이미지 초기화
    outImage = []

    # step2. outImage의 크기를 결정
    outH = inH;
    outW = inW

    # step3. 파일 크기 만큼 메모리 확보
    for i in range(0, outH):
        tmpList = []
        for k in range(0, outW):
            tmpList.append(0)
        outImage.append(tmpList)

    # step4. 영상처리 알고리즘 구현 부분
    # 영상 반전

    for i in range(inH):
        for k in range(inW):
            outImage[i][k] = abs(inImage[i][k]-255)

    displayImage(outImage)

def verMirroring():
    #영상 좌우 미러링
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage

    # step1. 출력 이미지 초기화
    outImage = []

    # step2. outImage의 크기를 결정
    outH = inH;
    outW = inW

    # step3. 파일 크기 만큼 메모리 확보
    for i in range(0, outH):
        tmpList = []
        for k in range(0, outW):
            tmpList.append(0)
        outImage.append(tmpList)

    # step4. 영상처리 알고리즘 구현 부분
    # 여기서는 좌우를 반전시킨다.

    index=0
    for i in range(inH):
        index=0
        for k in range(inW-1,0,-1):
            outImage[i][index] = inImage[i][k]
            index+=1
    displayImage(outImage)

def horMirroring():
    #영상 상하 미러링
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage

    # step1. 출력 이미지 초기화
    outImage = []

    # step2. outImage의 크기를 결정
    outH = inH;
    outW = inW

    # step3. 파일 크기 만큼 메모리 확보
    for i in range(0, outH):
        tmpList = []
        for k in range(0, outW):
            tmpList.append(0)
        outImage.append(tmpList)

    # step4. 영상처리 알고리즘 구현 부분
    # 여기서는 상하를 반전시킨다.

    index=0
    for i in range(inH-1, 0, -1):
        for k in range(inW):
            outImage[index][k] = inImage[i][k]
        index+=1
    displayImage(outImage)


def rotateImage():
    #영상 90도 회전
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage

    # step1. 출력 이미지 초기화
    outImage = []

    # step2. outImage의 크기를 결정
    outH = inH;
    outW = inW

    # step3. 파일 크기 만큼 메모리 확보
    for i in range(0, outH):
        tmpList = []
        for k in range(0, outW):
            tmpList.append(0)
        outImage.append(tmpList)

    # step4. 영상처리 알고리즘 구현 부분
    # 여기서는 90도 회전시킨다(시계방향)

    indexY=0
    for i in range(inH):
        indexX = inH - 1
        for k in range(inW):
            outImage[i][k] = inImage[indexX][indexY]
            indexX=indexX-1
        indexY+=1

    displayImage(outImage)


def trans2bwImage():
    #영상 흑백 변환
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage

    # step1. 출력 이미지 초기화
    outImage = []

    # step2. outImage의 크기를 결정
    outH = inH;
    outW = inW

    # step3. 파일 크기 만큼 메모리 확보
    for i in range(0, outH):
        tmpList = []
        for k in range(0, outW):
            tmpList.append(0)
        outImage.append(tmpList)

    # step4. 영상처리 알고리즘 구현 부분
    # 여기서는 흑백으로 변환된다.
    for i in range(inH):
        for k in range(inW):
            if inImage[i][k] > 127:
                outImage[i][k] = 255
            else:
                outImage[i][k]=0

    displayImage(outImage)


def twiceImage():
    #영상 확대(2배)
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage

    # step1. 출력 이미지 초기화
    outImage = []

    # step2. outImage의 크기를 결정
    outH = inH;
    outW = inW

    # step3. 파일 크기 만큼 메모리 확보
    for i in range(0, outH*2):
        tmpList = []
        for k in range(0, outW*2):
            tmpList.append(0)
        outImage.append(tmpList)

    # step4. 영상처리 알고리즘 구현 부분
    # 여기서는 2배 확대 -> 1셀이 차지하는 곳 : (0,0),(0,1), (1,0), (1,1)

    dx=[0,0,1,1]
    dy=[0,1,0,1]

    for i in range(inH):
        for k in range(inW):
            for idx in range(4):
                outImage[(2*i)+dx[idx]][(2*k)+dy[idx]] = inImage[i][k]

    displayImage(outImage, scope=2)

def halfImage():
    #영상 축소(2~8배)
    # 영상 확대(2배)
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage

    # step1. 출력 이미지 초기화
    outImage = []

    # step2. outImage의 크기를 결정
    outH = inH
    outW = inW

    # step3. 파일 크기 만큼 메모리 확보
    for i in range(0, outH ):
        tmpList = []
        for k in range(0, outW ):
            tmpList.append(0)
        outImage.append(tmpList)

    # step4. 영상처리 알고리즘 구현 부분
    # 여기서는 2배 확대 -> 1셀이 차지하는 곳 : (0,0),(0,1), (1,0), (1,1)

    dx = [0, 0, 1, 1]
    dy = [0, 1, 0, 1]

    for i in range(0,inH,2):
        for k in range(0,inW,2):
                outImage[int(0.5*i)][int(0.5 * k)] = inImage[i][k]

    displayImage(outImage, scope=0.5)



def saveImage():
    #image 저장

    pass


## Global Variables

window, canvas, paper=[None]*3
inW, inH, outW, outH=[400]*4
inImage=[]; outImage=[]


## MAIN
window= Tk();window.title("영상 데이터 분석/처리")

#메뉴 추가
mainMenu=Menu(window)
window.config(menu=mainMenu)

    #메뉴 1 : 파일
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='열기', command=openImage)
fileMenu.add_separator()
fileMenu.add_command(label='저장', command=None)

    #메뉴 2 : 영상처리1
imageMenu=Menu(mainMenu)
mainMenu.add_cascade(label='영상처리1', menu=imageMenu)
imageMenu.add_command(label='밝게하기', command=addImage)
imageMenu.add_separator()
imageMenu.add_command(label='어둡게하기', command=subImage)
imageMenu.add_separator()
imageMenu.add_command(label='영상 곱셈', command=mulImage)
imageMenu.add_separator()
imageMenu.add_command(label='영상 나눗셈', command=divImage)
imageMenu.add_separator()
imageMenu.add_command(label='영상 반전', command=reverseImage)
imageMenu.add_separator()
imageMenu.add_command(label='좌우 미러링', command=verMirroring)
imageMenu.add_separator()
imageMenu.add_command(label='상하 미러링', command=horMirroring)
imageMenu.add_separator()
imageMenu.add_command(label='회전(90도)', command=rotateImage)
imageMenu.add_separator()
imageMenu.add_command(label='흑백전환', command=trans2bwImage)
imageMenu.add_separator()
imageMenu.add_command(label='영상 확대', command=twiceImage)
imageMenu.add_separator()
imageMenu.add_command(label='영상 축소', command=halfImage)








window.mainloop()


