from tkinter import *
from tkinter.filedialog import *
import os.path
import math

###########################################################
########### RAW 데이터 분석#####################
###########################################################
## 함수 선언부
import xlwt


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

    ## 한 픽셀씩 화면에 출력 (열라 느림)
    # for i in range(outH) :
    #     for k in range(outW) :
    #         data = outImage[i][k]
    #         paper.put("#%02x%02x%02x" % (data, data, data), (k, i))
    ## 메모리에 화면(문자열)을 출력해 놓고, 한방에 출력(열라 빠름)
    rgbString = '' # 여기에 전체 픽셀 문자열을 저장할 계획
    step = 1
    for i in range(0, outH, step) :
        tmpString = ''
        for k in range(0, outW, step) :
            data = outImage[i][k]
            tmpString += ' #%02x%02x%02x' % (data, data, data)
        rgbString += '{' + tmpString + '} '
    paper.put(rgbString)


    canvas.pack()

import struct
def saveFile() :
    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH
    saveFp = asksaveasfile(parent=window, mode='wb',
                               defaultextension="*.raw", filetypes=(("RAW파일", "*.raw"), ("모든파일", "*.*")))
    for i in range(outW):
        for k in range(outH):
            saveFp.write( struct.pack('B',outImage[i][k]))

    saveFp.close()

import pymysql
from tkinter import ttk
IP_ADDR = '192.168.111.141'
DB_NAME = 'machineDB'
TBL_NAME = 'imageTBL'
USER_NAME = 'root'
USER_PASS = '1234'
def loadDB() :
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage
    global window2, sheet, rows
    con = pymysql.connect(host=IP_ADDR, user=USER_NAME, password=USER_PASS, database=DB_NAME, charset='utf8')
    cur = con.cursor()

    sql = "SELECT id, fName, fType FROM imageTBL"  # ID로 추출하기
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
    sql = "SELECT fName, image FROM imageTBL WHERE id=" + str(id) # ID로 이미지 추출하기
    cur.execute(sql)
    row = cur.fetchone()
    cur.close()
    con.close()
    import tempfile
    # 임시 폴더
    fname, binData = row
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

## RAW 영상의 입력 및 출력 평균값 계산
def averageRAW() :
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage
    rawSum =0
    for i in range(inH) :
        for k in range(inW) :
            rawSum += inImage[i][k]
    inRawAvg = rawSum // (inH * inW) # 입력영상 평균값
    rawSum = 0
    for i in range(outH):
        for k in range(outW):
            rawSum += outImage[i][k]
    outRawAvg = rawSum // (inH * inW)  # 출력영상 평균값

    subWindow = Toplevel(window);    subWindow.geometry('200x100')
    label1 = Label(subWindow, text='입력영상 평균값-->' + str(inRawAvg)); label1.pack()
    label2 = Label(subWindow, text='출력영상 평균값-->' + str(outRawAvg)); label2.pack()
    subWindow.mainloop()

## RAW 영상의 히스토그램 그리기
def histoRAW() :
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage
    countList = [0] * 256 ; normalList = [0] * 256
    # 빈도수 세기
    for i in range(outH):
        for k in range(outW):
            value = outImage[i][k]
            countList[value] += 1
    # 정규화 시키기 : 정규화된값 = (카운트값 - 최소값) * 최대높이 / (최대값 - 최소값)
    maxValue = max(countList);  minValue = min(countList)
    for i in range(len(countList)) :
        normalList[i] = (countList[i] - minValue) * 256 / (maxValue - minValue)
    # 히스토그램 그리기
    subWindow = Toplevel(window);    subWindow.geometry('256x256')
    subCanvas = Canvas(subWindow, width=256, height=256)
    subPaper = PhotoImage(width=256, height=256)
    subCanvas.create_image( (256/2, 256/2), image=subPaper, state='normal')

    for i in range(0, 256) :
        for k in range(0, int(normalList[i])) :
            if k > 255 :
                break
            data = 0
            subPaper.put('#%02x%02x%02x' % (data, data, data), (i, 255-k))

    subCanvas.pack(expand=1, anchor=CENTER)
    subWindow.mainloop()

import matplotlib.pyplot as plt
def matHistoRAW() :
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage
    countList = [0] * 256 ;
    # 빈도수 세기
    for i in range(outH):
        for k in range(outW):
            value = outImage[i][k]
            countList[value] += 1
    plt.plot(countList)
    plt.show()

###########################################################
###########CSV 데이터 분석#####################
###########################################################
csvList = []
def openCSVFile() :
    global  csvList
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage
    filename = askopenfilename(parent=window, filetypes=(("CSV 파일", "*.csv"), ("모든 파일", "*.*")))
    if filename == "" or filename == None:
        return

    loadCSV(filename)
import csv
def loadCSV(fname) :
    global csvList
    with open(fname, 'r', newline='') as filereader:
        csvReader = csv.reader(filereader) # CSV 전용으로 다시 열기
        header_list = next(csvReader)
        csvList.append(header_list)
        for  row_list in csvReader :
            csvList.append(row_list)

    drawSheet(csvList)

sheet = None
def drawSheet(cList) :
    global sheet
    if sheet != None :
        sheet.destroy()

    sheet = ttk.Treeview(window)
    sheet.pack(side=LEFT, fill=Y)

    sheet.column("#0", width=80); sheet.heading("#0", text=cList[0][0])
    sheet["columns"] = cList[0][1:]
    for colName in cList[0][1:]:
        sheet.column(colName, width=80); sheet.heading(colName, text=colName)

    for row in cList[1:] :
        colList = []
        for col in row[1:]:
            colList.append(col)
        sheet.insert('', 'end', text=row[0], values=tuple(colList))

def csvUp10() :
    global csvList
    # cost 열의 위치를 찾자.
    header_list = csvList[0]
    for i in range(len(header_list)) :
        header_list[i] = header_list[i].upper().strip()
    try :
        pos = header_list.index('COST')
    except :
        messagebox.showinfo('메시지', 'COST 열 없음')
        return

    for i in range(1, len(csvList)) :
        row = csvList[i]
        cost = row[pos]
        cost = float(cost[1:])
        cost *= 1.1
        cost_str = "${0:.2f}".format(cost)
        csvList[i][pos] = cost_str

    drawSheet(csvList)

def saveCSVFile() :
    global csvList
    saveFp = asksaveasfile(parent=window, mode='w',
                           defaultextension=".csv", filetypes=(("CSV파일", "*.csv"), ("모든파일", "*.*")))
    with open(saveFp.name, 'w', newline='') as filewriter :
        for row_list in csvList :
            row_str = ','.join(map(str, row_list)) # 리스트 --> ,로 구분된 스트링으로 만들기
            filewriter.writelines(row_str + '\n')

import xlrd
def openExcelFile() :
    global csvList
    global window, canvas, paper, inW, inH, outW, outH, inImage, outImage
    filename = askopenfilename(parent=window, filetypes=(("xls 파일", "*.xls;*.xlsx"), ("모든 파일", "*.*")))
    if filename == "" or filename == None:
        return
    workbook = xlrd.open_workbook(filename)
    sheetCount = workbook.nsheets

    firstYN = True
    for worksheet in workbook.sheets() :
        sRow = worksheet.nrows
        sCol = worksheet.ncols
        for i in range(sRow) :
            if firstYN == True and i == 0 :
                firstYN = False
                pass
            elif firstYN == False and i != 0 :
                pass
            elif firstYN == False and i == 0 :
                print(i, end='   ')
                continue
            tmpList = []
            for k in range(sCol) :
                value = worksheet.cell_value(i,k)
                tmpList.append(value)
            csvList.append(tmpList)

    drawSheet(csvList)

def saveExcelFile() :
    global csvList
    if csvList==[] or csvList==None:
        return
    saveFp = asksaveasfile(parent=window, mode='w',
                           defaultextension=".xls", filetypes=(("엑셀 파일", "*.xls"), ("모든파일", "*.*")))
    filename=saveFp.name

    workbook = xlwt.Workbook()
    outSheet = workbook.add_sheet('sheet1')
    for i in range(len(csvList)):
        for k in range(len(csvList[i])):
            outSheet.write(i,k,csvList[i][k])

    workbook.save(filename)
    messagebox.showinfo('저장완료',filename+"저장됨")
def excelUp10() :
    pass


## 전역 변수 선언부
window, canvas, paper = [None] * 3;  inW, inH, outW, outH = [200] * 4
inImage, outImage = [], []

## 메인 코드부
window = Tk(); window.title('빅데이터 분석/처리 통합 툴 (Ver 0.04)')
window.geometry('800x500')

## 메뉴 추가하기
mainMenu = Menu(window) # 메뉴 전체 껍질
window.config(menu=mainMenu)

rawDataMenu = Menu(mainMenu)
mainMenu.add_cascade(label="RAW 데이터 분석", menu=rawDataMenu)

rawfileMenu = Menu(rawDataMenu)
rawDataMenu.add_cascade(label="파일", menu=rawfileMenu)
rawfileMenu.add_command(label="파일에서 열기", command=openImage)
rawfileMenu.add_command(label="DB에서 불러오기", command=loadDB)
rawfileMenu.add_separator()
rawfileMenu.add_command(label="저장", command=saveFile)

rawImage1Menu = Menu(rawDataMenu)
rawDataMenu.add_cascade(label="영상처리1", menu=rawImage1Menu)
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
rawStatMenu.add_command(label="히스토그램(MatPlotLib)", command=matHistoRAW)
#################################
ecDataMenu = Menu(mainMenu)
mainMenu.add_cascade(label="엑셀(CSV) 데이터 분석", menu=ecDataMenu)

csvfileMenu = Menu(ecDataMenu)
ecDataMenu.add_cascade(label="CSV 분석", menu=csvfileMenu)
csvfileMenu.add_command(label="CSV 파일 열기", command=openCSVFile)
csvfileMenu.add_command(label="CSV 파일 저장", command=saveCSVFile)
csvfileMenu.add_separator()
csvfileMenu.add_command(label="가격10%인상", command=csvUp10)

excelfileMenu = Menu(ecDataMenu)
ecDataMenu.add_cascade(label="엑셀 분석", menu=excelfileMenu)
excelfileMenu.add_command(label="엑셀 파일 열기", command=openExcelFile)
excelfileMenu.add_command(label="엑셀 파일 저장", command=saveExcelFile)
excelfileMenu.add_separator()
excelfileMenu.add_command(label="가격10%인상", command=excelUp10)
window.mainloop()