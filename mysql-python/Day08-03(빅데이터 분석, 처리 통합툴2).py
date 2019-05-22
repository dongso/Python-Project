import tempfile
from tkinter import ttk
from tkinter.filedialog import *
import os.path
import math
import struct
import pymysql
from tkinter.simpledialog import *


## 전역 변수 선언부
window, canvas, paper = [None] * 3;  inW, inH, outW, outH = [200] * 4
inImage, outImage = [], []

IP_ADDR = '192.168.111.141'
DB_NAME = 'machinedb'
TBL_NAME = 'machinetbl'
USER_NAME = 'root'
USER_PASS = '1234'


## 함수 선언부
def loadImage(fname) :
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage
    inImage = [] # 초기화
    # 파일 크기 계산
    fsize = os.path.getsize(fname) # Byte 단위
    inW = inH = int(math.sqrt(fsize))
    # 빈 메모리 확보 (2차원 리스트)
    for _ in range(inH) :
        tmp = []
        for _ in range(inW) :
            tmp.append(0)
        inImage.append(tmp)
    # 파일 --> 메모리로 한개씩 옮기기
    fp = open(fname, 'rb')
    for  i  in  range(inH) :
        for k in range(inW) :
            data = int(ord(fp.read(1))) # 1개 픽셀값을 읽음 (0~255)
            inImage[i][k] = data
    fp.close()


def  openImage() :
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage
    filename = askopenfilename(parent=window, filetypes=(("RAW 파일", "*.raw"), ("모든 파일", "*.*")))
    if filename == "" or filename == None :
        return


    # 파일 --> 메모리
    loadImage(filename)

    # Input --> outPut으로 동일하게 만들기.
    equalImage()

def displayImage() :
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage
    if canvas != None :
        canvas.destroy()
    window.geometry(str(outH) + 'x' + str(outW))
    canvas = Canvas(window, height=outH, width=outW)
    paper = PhotoImage(height=outH, width=outW)
    canvas.create_image((outW / 2, outH / 2), image=paper, state='normal')

    # 기존 방법 : 한 셀식 화면에 출력(속도가 많이 느리다)
    # for i in range(outH) :
    #     for k in range(outW) :
    #         data = outImage[i][k]
    #         paper.put("#%02x%02x%02x" % (data, data, data), (k, i))


    # 속도 개선방법1. 메모리에 캐싱하기
    rgbString='' # 여기에 전체 픽셀 문자열을 저장할 계획이다.
    step=1
    for i in range(0, outH, step):
        tmpString=''
        for k in range(0, outW, step):
            data=outImage[i][k]
            tmpString+=" #%02x%02x%02x" % (data, data, data) #Gray Scale
        rgbString+='{'+tmpString+'} '

    paper.put(rgbString)
    canvas.pack()

def sheetDoubleClick(event):
    # Double Click Event
    global window2, sheet,rows
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage

    item = sheet.identify('item', event.x, event.y) #'I001',...
    entNum = int(item[1:]) -1 ## 쿼리 결과 리스트의 순번
    idx= rows[entNum][0] # 선택한 id

    window2.destroy() # 창닫기


    #DB에서 이미지를 다운로드

    con = pymysql.connect(host=IP_ADDR, user=USER_NAME, password=USER_PASS, db=DB_NAME, charset='utf8')
    cur = con.cursor()

    sql = "select fname, image from machinetbl where id="+str(idx)
    cur.execute(sql)

    row = cur.fetchone()
    fName,binData=row

# step 1. '임시 폴더/파일명' 지정
    fullPath = tempfile.gettempdir() + '/' + fName
# step 2. file open
    fp = open(fullPath, 'wb')
# step 3. Write file(save file)
    fp.write(binData)
# step 4. Close file
    fp.close


    if(fName.split('.')[1].upper() != 'RAW'):
        messagebox.showinfo('못봄', fName+'은 못봐요ㅠㅠ')
        return

    loadImage(fullPath)
    equalImage()

    cur.close()
    con.close()

def loadDB():
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage
    # 파일 다운로드


    con = pymysql.connect(host=IP_ADDR, user=USER_NAME, password=USER_PASS, db=DB_NAME, charset='utf8')
    cur = con.cursor()

    sql = "select id, fname, fType from machinetbl"
    cur.execute(sql)

    global rows; rows=cur.fetchall()



    # 새로운 윈도우 창 띄우기

    global window2; window2 = Tk(); window2.title('파일선택')
    global sheet; sheet = ttk.Treeview(window2, height=10);sheet.pack()


    #열 정보 조회
    descs= cur.description
    colNames = [d[0] for d in descs]
    sheet.column("#0", width=80)
    sheet.heading("#0", text=colNames[0])
    sheet['columns'] = colNames[1:]

    for colName in colNames[1:]:
        sheet.column(colName, width=80)
        sheet.heading(colName, text=colName)

    for row in rows:
        sheet.insert('','end', text=row[0], values=row[1:])

    sheet.bind('<Double-1>', sheetDoubleClick)



    window2.mainloop()




    cur.close()
    con.close()


######################################################################################################################
def equalImage() :
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage
    outImage = []  # 초기화
    # outImage의 크기를 결정
    outH = inH;  outW = inW
    # 빈 메모리 확보 (2차원 리스트)
    for _ in range(outH):
        tmp = []
        for _ in range(outW):
            tmp.append(0)
        outImage.append(tmp)
    #### 영상 처리 알고리즘을 구현 ####
    for i in range(inH) :
        for k in range(inW) :
            outImage[i][k] = inImage[i][k]
    ################################
    displayImage()

def addImage() :
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage
    outImage = []  # 초기화
    # outImage의 크기를 결정
    outH = inH;  outW = inW
    # 빈 메모리 확보 (2차원 리스트)
    for _ in range(outH):
        tmp = []
        for _ in range(outW):
            tmp.append(0)
        outImage.append(tmp)
    value = askinteger("밝게할 값", "값 입력")
    #### 영상 처리 알고리즘을 구현 ####
    for i in range(inH) :
        for k in range(inW) :
            if inImage[i][k] + value > 255 :
                outImage[i][k] = 255
            else :
                outImage[i][k] = inImage[i][k] + value
    ################################
    displayImage()

def reverseImage() :
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage
    outImage = []  # 초기화
    # outImage의 크기를 결정
    outH = inH;  outW = inW
    # 빈 메모리 확보 (2차원 리스트)
    for _ in range(outH):
        tmp = []
        for _ in range(outW):
            tmp.append(0)
        outImage.append(tmp)
    #### 영상 처리 알고리즘을 구현 ####
    for i in range(inH) :
        for k in range(inW) :
            outImage[i][k] = 255 - inImage[i][k]
    ################################
    displayImage()

def mirror1Image() :
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage
    outImage = []  # 초기화
    # outImage의 크기를 결정
    outH = inH;  outW = inW
    # 빈 메모리 확보 (2차원 리스트)
    for _ in range(outH):
        tmp = []
        for _ in range(outW):
            tmp.append(0)
        outImage.append(tmp)
    #### 영상 처리 알고리즘을 구현 ####
    for i in range(inH) :
        for k in range(inW) :
            outImage[inW-1-i][k] = inImage[i][k]
    ################################
    displayImage()

def bwImage() :
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage
    outImage = []  # 초기화
    # outImage의 크기를 결정
    outH = inH;  outW = inW
    # 빈 메모리 확보 (2차원 리스트)
    for _ in range(outH):
        tmp = []
        for _ in range(outW):
            tmp.append(0)
        outImage.append(tmp)
    #### 평균값 구하기 ###
    hap = 0
    for i in range(inH) :
        for k in range(inW) :
            hap += inImage[i][k]
    avg = hap // (inH * inW)

    #### 영상 처리 알고리즘을 구현 ####
    for i in range(inH) :
        for k in range(inW) :
            if inImage[i][k] >= avg :
                outImage[i][k] = 255
            else :
                outImage[i][k] = 0
    ################################
    displayImage()

def zoomOut1Image() :
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage
    outImage = []  # 초기화
    scale = askinteger("축소 값", "값 입력")
    # outImage의 크기를 결정
    outH = inH//scale;  outW = inW//scale
    # 빈 메모리 확보 (2차원 리스트)
    for _ in range(outH):
        tmp = []
        for _ in range(outW):
            tmp.append(0)
        outImage.append(tmp)
    #### 영상 처리 알고리즘을 구현 ####
    for i in range(inH) :
        for k in range(inW) :
            outImage[i//scale][k//scale] = inImage[i][k]
    ################################
    displayImage()

def zoomOut2Image() :
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage
    outImage = []  # 초기화
    scale = askinteger("축소 값", "값 입력")
    # outImage의 크기를 결정
    outH = inH//scale;  outW = inW//scale
    # 빈 메모리 확보 (2차원 리스트)
    for _ in range(outH):
        tmp = []
        for _ in range(outW):
            tmp.append(0)
        outImage.append(tmp)
    #### 영상 처리 알고리즘을 구현 ####
    for i in range(outH) :
        for k in range(outW) :
            outImage[i][k] = inImage[i*scale][k*scale]
    ################################
    displayImage()

def zoomIn1Image() :
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage
    outImage = []  # 초기화
    scale = askinteger("축소 값", "값 입력")
    # outImage의 크기를 결정
    outH = inH*scale;  outW = inW*scale
    # 빈 메모리 확보 (2차원 리스트)
    for _ in range(outH):
        tmp = []
        for _ in range(outW):
            tmp.append(0)
        outImage.append(tmp)
    #### 영상 처리 알고리즘을 구현 ####
    for i in range(inH) :
        for k in range(inW) :
            outImage[i*scale][k*scale] = inImage[i][k]
    ################################
    displayImage()


def zoomIn2Image() :
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage
    outImage = []  # 초기화
    scale = askinteger("축소 값", "값 입력")
    # outImage의 크기를 결정
    outH = inH*scale;  outW = inW*scale
    # 빈 메모리 확보 (2차원 리스트)
    for _ in range(outH):
        tmp = []
        for _ in range(outW):
            tmp.append(0)
        outImage.append(tmp)
    #### 영상 처리 알고리즘을 구현 ####
    for i in range(outH) :
        for k in range(outW) :
            outImage[i][k] = inImage[i//scale][k//scale]
    ################################
    displayImage()

def saveFile() :
    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH
    saveFp = asksaveasfile(parent=window, mode='wb',
                               defaultextension="*.raw", filetypes=(("RAW파일", "*.raw"), ("모든파일", "*.*")))
    for i in range(outW):
        for k in range(outH):
            saveFp.write( struct.pack('B',outImage[i][k]))

    saveFp.close()



## 메인 코드부
window = Tk(); window.title('빅데이터 분석/처리 통합 툴(Ver 0.02)')


## 메뉴 추가하기
mainMenu = Menu(window) # 메뉴 전체 껍질
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="파일에서 열기", command=openImage)
fileMenu.add_command(label="DB에서 불러오기", command=loadDB)

fileMenu.add_separator()
fileMenu.add_command(label="저장", command=saveFile)

image1Menu = Menu(mainMenu)
mainMenu.add_cascade(label="영상처리1", menu=image1Menu)
image1Menu.add_command(label="밝게하기", command=addImage)
image1Menu.add_command(label="반전하기", command=reverseImage)
image1Menu.add_command(label="미러링(상하)", command=mirror1Image)
image1Menu.add_command(label="흑백", command=bwImage)
image1Menu.add_command(label="축소(포워딩)", command=zoomOut1Image)
image1Menu.add_command(label="축소(백워딩)", command=zoomOut2Image)
image1Menu.add_command(label="확대(포워딩)", command=zoomIn1Image)
image1Menu.add_command(label="확대(백워딩)", command=zoomIn2Image)

window.mainloop()