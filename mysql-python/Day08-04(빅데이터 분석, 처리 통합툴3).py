from tkinter import *
from tkinter.filedialog import *
import os.path
import math
import tempfile
import struct
import pymysql
from tkinter import ttk
import matplotlib.pyplot as plt
import csv
import xlrd
import xlwt

IP_ADDR = '192.168.111.141'
DB_NAME = 'machinedb'
TBL_NAME = 'machinetbl'
USER_NAME = 'root'
USER_PASS = '1234'

## 함수 선언부


#########################################################################################
############################RAW 데이터 분석################################################
#########################################################################################

def listToraw(step=1):
    global outImage
    rgbString = ''  # 여기에 전체 픽셀 문자열을 저장할 계획

    for i in range(0, outH, step):
        tmpString = ''
        for k in range(0, outW, step):
            data = outImage[i][k]
            tmpString += ' #%02x%02x%02x' % (data, data, data)
        rgbString += '{' + tmpString + '} '
    return rgbString

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
    global fname; fname = askopenfilename(parent=window, filetypes=(("RAW 파일", "*.raw"), ("모든 파일", "*.*")))
    if fname == "" or fname == None :
        return


    # 파일 --> 메모리
    loadImage(fname)

    # Input --> outPut으로 동일하게 만들기.
    equalImage()

    fname=fname.split('/')[len(fname.split('/'))-1] #DB 저장이름

def displayImage() :
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage
    if canvas != None :
        canvas.destroy()
    window.geometry(str(outH) + 'x' + str(outW))
    canvas = Canvas(window, height=outH, width=outW)
    paper = PhotoImage(height=outH, width=outW)
    canvas.create_image((outW / 2, outH / 2), image=paper, state='normal')

    ## 한 픽셀씩 화면에 출력 (열라 느림)
    # for i in range(outH) :
    #     for k in range(outW) :
    #         data = outImage[i][k]
    #         paper.put("#%02x%02x%02x" % (data, data, data), (k, i))
    ## 메모리에 화면(문자열)을 출력해 놓고, 한방에 출력(열라 빠름)


    #(함수 listToraw()로 만들어서 사용함.)
    # rgbString = '' # 여기에 전체 픽셀 문자열을 저장할 계획
    # step = 1
    # for i in range(0, outH, step) :
    #     tmpString = ''
    #     for k in range(0, outW, step) :
    #         data = outImage[i][k]
    #         tmpString += ' #%02x%02x%02x' % (data, data, data)
    #     rgbString += '{' + tmpString + '} '
    paper.put(listToraw())


    canvas.pack()

def saveFile() :
    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH
    saveFp = asksaveasfile(parent=window, mode='wb',
                               defaultextension="*.raw", filetypes=(("RAW파일", "*.raw"), ("모든파일", "*.*")))
    for i in range(outW):
        for k in range(outH):
            saveFp.write( struct.pack('B',outImage[i][k]))

    saveFp.close()


def loadDB() :
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage
    global window2, sheet, rows
    con = pymysql.connect(host=IP_ADDR, user=USER_NAME, password=USER_PASS, database=DB_NAME, charset='utf8')
    cur = con.cursor()

    sql = "SELECT id, fname, fType FROM machinetbl"  # ID로 추출하기
    cur.execute(sql)

    rows = cur.fetchall()

    ## 새로운 윈도창 띄우기
    window2 = Toplevel(window)
    sheet = ttk.Treeview(window2, height=10);    sheet.pack()
    descs = cur.description
    colNames = [d[0] for d in descs]
    sheet.column("#0", width=80);
    sheet.heading("#0", text=colNames[0])
    sheet["columns"] = colNames[1:]
    for colName in colNames[1:]:
        sheet.column(colName, width=80);
        sheet.heading(colName, text=colName)
    for row in rows :
        sheet.insert('', 'end', text=row[0], values=row[1:])
    sheet.bind('<Double-1>', sheetDblClick)

    cur.close()
    con.close()

def sheetDblClick(event) :
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage
    global window2, sheet, rows

    item = sheet.identify('item', event.x, event.y) # 'I001' ....
    entNum = int(item[1:]) - 1  ## 쿼리한 결과 리스트의 순번
    id = rows[entNum][0] ## 선택한 id
    window2.destroy()
    # DB에서 이미지를 다운로드
    con = pymysql.connect(host=IP_ADDR, user=USER_NAME, password=USER_PASS, database=DB_NAME, charset='utf8')
    cur = con.cursor()
    sql = "SELECT fName, image FROM machinetbl WHERE id=" + str(id) # ID로 이미지 추출하기
    cur.execute(sql)
    row = cur.fetchone()
    cur.close()
    con.close()

    # 임시 폴더
    global fname, binData; fname, binData = row
    fullPath = tempfile.gettempdir()+ '/' + fname # 임시경로 + 파일명
    fp = open(fullPath , 'wb') # 폴더를 지정.
    fp.write(binData)
    fp.close()

    if fname.split('.')[1].upper() != 'RAW' :
        messagebox.showinfo('못봄', fname + '은 못봐요.ㅠㅠ')
        return

    # 파일 --> 메모리
    loadImage(fullPath)
    equalImage()

def saveDB():
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage
    global window2, sheet, rows,fname, binData,filename
    con = pymysql.connect(host=IP_ADDR, user=USER_NAME, password=USER_PASS, database=DB_NAME, charset='utf8')
    cur = con.cursor()

    if fname != '' or fname != None :
        fName=fname.split('.')[0]+"_copy."+fname.split('.')[1]
        fType=fname.split('.')[1].upper()
    else :
        fName = filename.split('.')[0] + "_copy." + filename.split('.')[1]
        fType = filename.split('.')[1].upper()


    binImage=listToraw()

    sql="insert into machinetbl(fname, fType, image) values(%s, %s, %s)"
    tupleData=(fName, fType, binImage)
    cur.execute(sql,tupleData)

    cur.close()
    con.commit()
    con.close()

##################################################################################

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

from tkinter.simpledialog import *
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




##########################################################################
def averageRAW():
    #RAW 영상의 입력 및 출력 평균값 계산
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage

    rawSum=0
    for i in range(inH):
        for k in range(inW):
            rawSum+=inImage[i][k]
    inRawAvg=rawSum//(inH*inW) ##입력 영상 평균값

    rawSum = 0
    for i in range(outH):
        for k in range(outW):
            rawSum += outImage[i][k]
    outRawAvg=rawSum//(outH*outW) ## 출력 영상 평균값

    subWindow=Toplevel(window)
    subWindow.geometry('200x100')
    label1 = Label(subWindow, text='입력 영상 평균값-->'+str(inRawAvg)); label1.pack()
    label2 = Label(subWindow, text='출력 영상 평균값-->'+str(outRawAvg)); label2.pack()

    subWindow.mainloop()

def histoRAW():
    # RAW 영상의 히스토그램 그리기
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage

    countList=[0]*256; normalList=[0]*256

    #빈도수 계산
    for i in range(outH):
        for k in range(outW):
            countList[outImage[i][k]]+=1

    print(countList)

    #정규화 시키기 : 정규화된 값 = (카운트값-최소값) * 밝기최대값 / (최대값-최소값)
    maxValue=max(countList); minValue=min(countList)
    for i in range(len(countList)):
        normalList[i]=int((countList[i]-minValue)*256/(maxValue-minValue))
    #히스토그램 그리기
    subWindow = Toplevel(window)
    subWindow.geometry('256x256')

    subCanvas=Canvas(subWindow, width=256, height=256)
    subPaper=PhotoImage( width=256, height=256)
    subCanvas.create_image((256/2,256/2), image=subPaper, state='normal')

    for i in range(0,256):
        for k in range(0, normalList[i]):
            if k>=255 :
                break
            data=0
            subPaper.put('#%02x%02x%02x'%(data,data,data), (i,255-k))

    subCanvas.pack(expand=1, anchor=CENTER)
    subWindow.mainloop()

def matHistoRAW():
    # RAW 영상의 히스토그램 그리기
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage

    countList=[0]*256; normalList=[0]*256

    #빈도수 계산
    for i in range(outH):
        for k in range(outW):
            countList[outImage[i][k]]+=1

    plt.plot(countList)
    plt.show()

#########################################################################################
############################CSV 데이터 분석################################################
#########################################################################################
csvList=[]
def openCSVFile():
    global csvList
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage
    global fname;
    fname = askopenfilename(parent=window, filetypes=(("CSV 파일", "*.csv"), ("모든 파일", "*.*")))
    if fname == "" or fname == None:
        return

    # 파일 --> 메모리
    loadCSV(fname)

sheet=None
def loadCSV(filename):
    # client의 파일을 오픈한 뒤 화면에 출력하는 함수를 Call
    global csvList,sheet

    with open(filename,'r', newline='') as fileReader:
        csvReader=csv.reader(fileReader) # CSV 전용으로 다시 파일 오픈
        headerList=next(csvReader)
        csvList.append(headerList) # csv 파일의 헤더를 추가한다.

        for rowList in csvReader: # csv파일의 내용을 추가한다.
            csvList.append(rowList)

    print(csvList)
    drawSheet(csvList)

sheet=None
def drawSheet(csvList):
    # csv파일의 내용을 화면에 출력
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage
    global sheet
    if sheet!=None:
        sheet.destroy()
    sheet=ttk.Treeview(window)
    sheet.pack(side=LEFT, fill=Y)
    sheet.column("#0", width=80);
    sheet.heading("#0", text=csvList[0][0])
    sheet["columns"] = csvList[0][1:]

    for colName in csvList[0][1:]:
        sheet.column(colName, width=80);sheet.heading(colName, text=colName)

    for row in csvList[1:]:
        colList = []
        for col in row[1:]:
            colList.append(col)
        sheet.insert('', 'end', text=row[0], values=tuple(colList))


def csvup10():
    global csvList
    headerList=csvList[0]

    for i in range(len(headerList)):
        headerList[i]=headerList[i].upper().strip() #대문자로 변환후 앞뒤 공백 제거

    try :
        pos=headerList.index("COST")
        print(pos)
    except:
        messagebox.showinfo('message', 'COST열 없음')
        return

    for i in range(1,len(csvList[1:])):
        row=csvList[i]
        cost=row[pos]
        cost=float(cost[1:])
        cost=round(cost*1.1,3) #해당 값을 10퍼센트 증가시킨다.
        cost="$"+str(cost)
        csvList[i][pos]=cost

    drawSheet(csvList)

def saveCSVFile():
    global csvList
    saveFp = asksaveasfile(parent=window, mode='w',
                               defaultextension="*.csv", filetypes=(("CSV파일", "*.csv"), ("모든파일", "*.*")))

    with open(saveFp.name, 'w', newline='') as fileWirter:
        for rowList in csvList:
            row_str=','.join(map(str, rowList)) #List->,로 구분된 스트링으로 만들게된다.
            fileWirter.writelines(row_str+'\n')


#########################################################################################
##########################EXCEL 데이터 분석################################################
#########################################################################################

def openEXCELFile():
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage
    global fname,csvList
    fname = askopenfilename(parent=window, filetypes=(("XLS 파일", "*.xls;*.xlsx"), ("모든 파일", "*.*")))

    if fname == "" or fname == None:
        return
    workbook = xlrd.open_workbook(fname)
    sheetCnt=workbook.nsheets

    firstYN=True
    for workSheet in workbook.sheets():
        sRow=workSheet.nrows
        sCol=workSheet.ncols
        for i in range(sRow):
            if firstYN == True and i == 0:
                firstYN=False
                pass
            elif firstYN == False and i != 0:
                pass
            elif firstYN ==False and i==0 :
                continue
            tmpList=[]
            for k in range(sCol):
                value=workSheet.cell_value(i,k)
                tmpList.append(value)
            csvList.append(tmpList)



    drawSheet(csvList)

def loadEXCEL(filename):

    pass
def saveEXCELFile():
    pass

def excelup10():
    pass


## 전역 변수 선언부
window, canvas, paper = [None] * 3;  inW, inH, outW, outH = [200] * 4
inImage, outImage = [], []

## 메인 코드부
window = Tk(); window.title('빅데이터 분석/처리 통합 툴 (Ver 0.02)'); window.geometry("1000x600")


## 메뉴 추가하기
mainMenu = Menu(window) # 메뉴 전체 껍질
window.config(menu=mainMenu)

rawDataMenu = Menu(mainMenu)
mainMenu.add_cascade(label="RAW 데이터 분석", menu=rawDataMenu)
rawfileMenu=Menu(rawDataMenu)
rawDataMenu.add_cascade(label="파일", menu=rawfileMenu)

rawfileMenu.add_command(label="파일에서 열기", command=openImage)
rawfileMenu.add_command(label="DB에서 불러오기", command=loadDB)
rawfileMenu.add_separator()
rawfileMenu.add_command(label="저장", command=saveFile)
#rawfileMenu.add_command(label="DB에 저장하기", command=saveDB)

rawImage1Menu = Menu(rawDataMenu)
rawDataMenu.add_cascade(label="영상처리1", menu=rawImage1Menu)
image1Menu=Menu(rawImage1Menu)
rawImage1Menu.add_command(label="밝게하기", command=addImage)
rawImage1Menu.add_command(label="반전하기", command=reverseImage)
rawImage1Menu.add_command(label="미러링(상하)", command=mirror1Image)
rawImage1Menu.add_command(label="흑백", command=bwImage)
rawImage1Menu.add_command(label="축소(포워딩)", command=zoomOut1Image)
rawImage1Menu.add_command(label="축소(백워딩)", command=zoomOut2Image)
rawImage1Menu.add_command(label="확대(포워딩)", command=zoomIn1Image)
rawImage1Menu.add_command(label="확대(백워딩)", command=zoomIn2Image)


rawStatMenu = Menu(rawDataMenu)
rawDataMenu.add_cascade(label="통계 분석", menu=rawStatMenu)
rawStatMenu.add_command(label="평균값", command=averageRAW)
rawStatMenu.add_command(label="히스토그램", command=histoRAW)
rawStatMenu.add_command(label="히스토그램(matPlotlib)", command=matHistoRAW)


# -- 새로운 메뉴 탭 추가(여러 파일 타입 분석, csv, excel)

ecDataMenu = Menu(mainMenu)
mainMenu.add_cascade(label="엑셀(csv)데이터 분석", menu=ecDataMenu)
csvfileMenu=Menu(ecDataMenu)
ecDataMenu.add_cascade(label="CSV 분석", menu=csvfileMenu)
csvfileMenu.add_command(label="csv파일 열기", command=openCSVFile)
csvfileMenu.add_command(label="csv파일 저장하기", command=saveCSVFile)
csvfileMenu.add_command(label="가격(cost) 10%인상시키기", command=csvup10)

excelfileMenu=Menu(ecDataMenu)
ecDataMenu.add_cascade(label="EXCEL 분석", menu=excelfileMenu)
excelfileMenu.add_command(label="excel파일 열기", command=openEXCELFile)
excelfileMenu.add_command(label="excel파일 저장하기", command=saveEXCELFile)
excelfileMenu.add_command(label="가격(cost) 10%인상시키기", command=excelup10)


window.mainloop()

