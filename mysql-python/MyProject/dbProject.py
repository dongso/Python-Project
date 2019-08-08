
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.simpledialog import askinteger

import matplotlib as plt
import pymysql
import DBConn
import printM
import Search
from tkinter import ttk, messagebox
import tempfile
from PIL import Image
import numpy as np
import cv2

#Global variables....
global window, variable, fullFrame, canvas, paper, itemList


def getItemidx(itemName):
    itemList=['shirts', 'pants', 'shoes', 'bag']  # 0,1,2,3,4
    cnt=0
    for item in itemList:
        if item ==itemName:
            break
        cnt+=1
    return cnt

def sear1():
    global variable, fullFrame,listIDX, listCOMM,listCOLOR, itemList

    cnt=getItemidx(variable.get())

    con = pymysql.connect(host=IP_ADDR, user=USER_NAME, password=USER_PASS, db=DB_NAME, charset='utf8')
    cur = con.cursor()

    query="select Cloths.mainColor, Cloths.comment from Cloths where categoryType in (select idx from Category where cname ='"+itemList[cnt]+"')"
    print(query)
    cur.execute(query)

    colorList, commentList,idxList=[],[],[]
    cnt=1
    while True:
        row = cur.fetchone()
        if row == None or row == "":
            break
        colorList.append(row[0])
        #cnameList.append(row[1])
        commentList.append(row[1])
        idxList.append(cnt)
        cnt+=1

    listIDX.delete(0, listIDX.size() - 1)
    listCOMM.delete(0, listCOMM.size() - 1)
    #listRECE.delete(0, listRECE.size() - 1)
    listCOLOR.delete(0, listCOLOR.size() - 1)


    for idx, color,  comment in zip(idxList,colorList, commentList):
        listIDX.insert(END, idx)
        listCOLOR.insert(END, color)
        #listRECE.insert(END, cname)
        listCOMM.insert(END, comment)

    cur.close()
    con.close()

    return

def menuSearch1():
    ######## MENU 1. 검색 ########

    global variable, fullFrame,listIDX, listCOMM,listCOLOR

    if fullFrame != None :
        fullFrame.destroy()

    fullFrame=Frame(window); fullFrame.pack()
    frame1 = Frame(fullFrame); frame1.pack()

    itemList = ['shirts', 'pants', 'shoes', 'bag']  # 0,1,2,3,4

    variable = StringVar(frame1)
    variable.set(itemList[0]) #initial value

    w=OptionMenu(frame1, variable, *itemList)
    w.pack(side=LEFT)
    btn1 = Button(frame1, text="검색", command=sear1);btn1.pack(side=RIGHT)


    ####### 검색 결과 화면 ######
    frame2 = Frame(fullFrame); frame2.pack(side=TOP, expand=1)
    idx=Label(frame2, text="번호");idx.pack(side=LEFT, padx=60)
    color=Label(frame2, text="메인 컬러");color.pack(side=LEFT, padx=40)
    cType=Label(frame2, text="형식");cType.pack(side=LEFT, padx=50)
    comment=Label(frame2, text="설명");comment.pack(side=LEFT, padx=40)

    frame3 = Frame(fullFrame); frame3.pack(side=BOTTOM, expand=1)
    listIDX=Listbox(frame3); listIDX.pack(side=LEFT)
    listCOLOR=Listbox(frame3); listCOLOR.pack(side=LEFT)
    #listRECE = Listbox(frame3); listRECE.pack(side=LEFT)
    listCOMM= Listbox(frame3); listCOMM.pack(side=LEFT)

    return



canvas,paper=None, None

IP_ADDR = '127.0.0.1'
DB_NAME = 'dbProject'
USER_NAME = 'root'
USER_PASS = '1234'


window = Tk(); window.title("모의 스타일링 툴(ver 1.0")
window.geometry("800x500")
fullFrame = Frame(window); fullFrame.pack()

itemList=['shirts', 'pants','shoes','bag']

####### Main Menu #######
mainMenu = Menu(window)
window.config(menu=mainMenu)


# Status Bar 추가
status = Label(window, text="이미지 정보:", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

######## MENU 1. 검색 ########
searchMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "검색", menu=searchMenu)

searchMenu.add_cascade(label="옷장 검색", command=menuSearch1)

######## MENU 2. 추가 ########
addMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "추가", menu=addMenu)
addMenu.add_cascade(label="옷 추가하기", command=None)

######## MENU 3. 옷 정보 검색 ########
clothsMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "옷 정보", menu=clothsMenu)

clothsMenu.add_cascade(label="가격 정보 검색", command=None)
clothsMenu.add_cascade(label="최근 착용일 검색", command=None)

######## MENU 4. 스타일링 ########
# styleMenu = Menu(mainMenu)
#
# sMenu=Menu(styleMenu)
#
# mainMenu.add_cascade(label = "스타일링", menu=styleMenu)
# styleMenu.add_cascade(label="action", menu=sMenu, command=None)
# sMenu.add_cascade(label = "스타일링", command=None)
# sMenu.add_cascade(label = "옷 색상 바꾸기", command=None)

######## MENU 5. 스타일 북 ########
styleBookMenu = Menu(mainMenu)

addStyleMenu=Menu(styleBookMenu)

mainMenu.add_cascade(label = "스타일 북", menu=styleBookMenu)
styleBookMenu.add_command(label="추가하기", command=None)
styleBookMenu.add_command(label="스타일 불러오기", command=None)

styleBookMenu.add_cascade(label="필터 적용하기", menu=addStyleMenu)
addStyleMenu.add_cascade(label ="필터1", command=None)
addStyleMenu.add_cascade(label ="필터2", command=None)

######## MENU 6. 프린트하기 ########
printMenu = Menu(mainMenu)

mainMenu.add_cascade(label="프린트하기", menu=printMenu)
printMenu.add_cascade(label="프린트하기", command=None) # filename 전달하기.


######## MENU 7. Image Processing ########
imageMenu = Menu(mainMenu)

mainMenu.add_cascade(label="이미지 프로세싱", menu=imageMenu)
imageMenu.add_cascade(label="배경제거", command=None) # filename 전달하기.

window.mainloop()