from tkinter import *
from tkinter.filedialog import askopenfilename

import pymssql

import DBConn
import printM
import Search
from tkinter import ttk, messagebox
import tempfile
from PIL import Image

global window

IP_ADDR = '192.168.111.130'
DB_NAME = 'khyProject'
USER_NAME = 'root'
USER_PASS = '1234'





window = Tk(); window.title("스타일링 툴(ver 0.0.1")
window.geometry("800x500")
fullFrame=Frame(window); fullFrame.pack()



# obj=DBConn.Connection()
# con, cur=obj.dbCONN()
#
#
# cur.close()
# con.commit()
# con.close()

def sear1():
    global variable

    category=variable.get()
    obj = Search.Searching()
    obj.setTable("Cloths")

    # print(obj.getTable())
    query = "select Cloths.mainColor, Category.cname, Cloths.comment from Cloths, Category where Category.cname='" + category + "'"
    obj.setQuery(query)

    print(obj.getQuery())



def menuSearch1():
    ######## MENU 1. 검색 ########

    global variable, fullFrame

    if fullFrame != None :
        fullFrame.destroy()

    fullFrame=Frame(window); fullFrame.pack()
    frame1 = Frame(fullFrame); frame1.pack()

    itemList=['상의','하의','모자','신발','가방']

    variable = StringVar(frame1)
    variable.set(itemList[0]) #initial value

    w=OptionMenu(frame1, variable, *itemList)
    w.pack(side=LEFT)
    btn1 = Button(frame1, text="검색", command=sear1);btn1.pack(side=RIGHT)

    #print(variable.get())

    ####### 검색 결과 화면 ######
    frame2 = Frame(fullFrame); frame2.pack(side=TOP, expand=1)
    idx=Label(frame2, text="번호");idx.pack(side=LEFT, padx=60)
    comm=Label(frame2, text="설명");comm.pack(side=LEFT, padx=40)
    rece=Label(frame2, text="최근 착용일");rece.pack(side=LEFT, padx=50)
    image=Label(frame2, text="이미지 보기");image.pack(side=LEFT, padx=40)

    frame3 = Frame(fullFrame); frame3.pack(side=BOTTOM, expand=1)
    listIDX=Listbox(frame3); listIDX.pack(side=LEFT)
    listCOMM=Listbox(frame3); listCOMM.pack(side=LEFT)
    listRECE = Listbox(frame3); listRECE.pack(side=LEFT)
    listImage= Listbox(frame3); listImage.pack(side=LEFT)

    return


def makeEmptyRGBList():

    global fullFrame, inW, inH

    R, G, B = [], [], []  # 초기화
    for _ in range(inH):
        tmp = []
        for _ in range(inW):
            tmp.append(0)
        R.append(tmp)
    for _ in range(inH):
        tmp = []
        for _ in range(inW):
            tmp.append(0)
        G.append(tmp)
    for _ in range(inH):
        tmp = []
        for _ in range(inW):
            tmp.append(0)
        B.append(tmp)
    return R,G,B



def loadImage(fname):
    global fullFrame, inW, inH,inImageR, inImageG, inImageB,text
    photo=Image.open(fname)
    inW = photo.width; inH=photo.height

    inImageR, inImageG, inImageB=[],[],[]
    inImageR, inImageG, inImageB =makeEmptyRGBList()

    photoRGB = photo.convert('RGB')
    text=""
    for i in range(inH):
        for k in range(inW):
            r, g, b = photoRGB.getpixel((k, i))  #
            inImageR[i][k] = r;
            inImageG[i][k] = g;
            inImageB[i][k] = b
            text+="("+str(r)+","+str(g)+","+str(b)+") "
            #(r,g,b) (r,g,b) (r,g,b) ...

    print("load image done...")
    return


def openImage():
    global fullFrame, inW, inH, outW, outH, inImageR, inImageG, inImageB, outImageR, outImageG, outImageB, filename
    filename = askopenfilename(parent=fullFrame, filetypes=(("영상 파일", "*.gif;*.jpg;*.png;*.bmp;*.tif"), ("모든 파일", "*.*")))
    if filename == "" or filename == None:
        return
    # 파일 --> 메모리
    loadImage(filename)


def addCloths():
    global variable,fullFrame,variable,ent1,ent2, w, inW, inH, outW, outH, inImageR, inImageG, inImageB, outImageR, outImageG, outImageB, filename,text
    itemList=['상의','하의','신발','가방'] #0,1,2,3,4

    con = pymssql.connect(host=IP_ADDR, user=USER_NAME, password=USER_PASS, database=DB_NAME,
                          charset='utf8')
    cur = con.cursor()


    cnt=0
    for item in itemList:
        if item==variable.get():
            break
        cnt+=1


    categoryType=str(cnt+1)
    mC=str(ent1.get())
    comment=str(ent2.get())

    query="insert into Cloths(mainColor, categoryType, comment) values('"+mC+"', "+categoryType+", '"+comment+"')"

    cur.execute(query)
    print(query)

    query = "select max(idx) from Cloths"
    cur.execute(query)
    maxIdx=str(cur.fetchone()[0])

    query = "insert into Image(cloth_idx, width, height, imageInfo) values("+maxIdx+", "+str(inW)+", "+str(inH)+",'"+text+"')"

    cur.execute(query)


    cur.close()
    con.commit()
    con.close()

def menuAdd1():
    ######## MENU 2. 추가 ########

    global variable,fullFrame,variable,ent1,ent2,w

    if fullFrame != None:
        fullFrame.destroy()


    fullFrame=Frame(window); fullFrame.pack()


    frame1 = Frame(fullFrame); frame1.pack(side=TOP)

    itemList=['상의','하의','신발','가방']

    variable = StringVar(frame1)
    variable.set(itemList[0]) #initial value

    w=OptionMenu(frame1, variable, *itemList)
    w.pack(side=LEFT)

    ent1 = Entry(frame1); ent1.pack(side=LEFT, padx=10) #input Main color
    ent2 = Entry(frame1); ent2.pack(side=LEFT, padx=10) #input comment

    btn1 = Button(frame1, text="추가", command=addCloths);btn1.pack(side=LEFT, padx=10)


    frame2 = Frame(fullFrame); frame2.pack(side=BOTTOM)
    #label1 = Label(frame2); label1.pack()

    btn2 = Button(frame2, text="이미지 불러오기",command=openImage); btn2.pack(side=LEFT, padx=10)
    return

def sear2():
    global variable, fullFrame
    con = pymssql.connect(host=IP_ADDR, user=USER_NAME, password=USER_PASS, database=DB_NAME,
                          charset='utf8')
    cur = con.cursor()

    itemList=['상의','하의','신발','가방'] #0,1,2,3,4

    itemIdx = 0
    for item in itemList:
        if item == variable.get():
            break
        itemIdx += 1
    itemIdx+=1

    query="select items, wearDate from wearing order by wearDate desc"
    cur.execute(query)
    rows=cur.fetchall()

    iList=[]
    dateList=[]
    for row in rows:
        iList.append(row[0]) ## 입은 옷 저장.
        dateList.append(row[1]) ## 입은 날짜 저장.

    for item in iList:
        print(item)




    cur.close()
    con.commit()
    con.close()
    return


def menuPrice():
    ######## MENU 3. 옷 정보 검색-가격 ########

    global variable, fullFrame

    if fullFrame != None:
        fullFrame.destroy()

    fullFrame = Frame(window);
    fullFrame.pack()
    frame1 = Frame(fullFrame);
    frame1.pack()

    itemList = ['상의','하의','신발','가방']

    variable = StringVar(frame1)
    variable.set(itemList[0])  # initial value

    w = OptionMenu(frame1, variable, *itemList)
    w.pack(side=LEFT)
    btn1 = Button(frame1, text="검색", command=sear2);
    btn1.pack(side=RIGHT)

    # print(variable.get())

    ####### 검색 결과 화면 ######
    frame2 = Frame(fullFrame);
    frame2.pack(side=TOP, expand=1)
    idx = Label(frame2, text="번호");idx.pack(side=LEFT, padx=60)
    comm = Label(frame2, text="설명");comm.pack(side=LEFT, padx=40)
    rece = Label(frame2, text="최근 착용일");rece.pack(side=LEFT, padx=50)
    image = Label(frame2, text="가격");image.pack(side=LEFT, padx=40)

    frame3 = Frame(fullFrame);
    frame3.pack(side=BOTTOM, expand=1)
    listIDX = Listbox(frame3);
    listIDX.pack(side=LEFT)
    listCOMM = Listbox(frame3);
    listCOMM.pack(side=LEFT)
    listRECE = Listbox(frame3);
    listRECE.pack(side=LEFT)
    listImage = Listbox(frame3);
    listImage.pack(side=LEFT)

    return

def menuRecent():
    ######## MENU 3. 옷 정보 검색 - 최근 착용일 ########
    global variable, fullFrame, sheet, rows, window2

    if fullFrame != None:
        fullFrame.destroy()

    fullFrame = Frame(window);
    fullFrame.pack()

    obj=Search.Searching()
    con, cur=obj.getDBcon()

    obj.setTable="Wearing"
    query="select items from "+obj.getTable()+" order by wearDate Desc"

    obj.setQuery(query)

    rows=cur.fetchall()

    ## 새로운 윈도창 띄우기
    window2 = Toplevel(fullFrame)
    sheet = ttk.Treeview(window2, height=10);
    sheet.pack()
    descs = cur.description
    colNames = [d[0] for d in descs]
    sheet.column("#0", width=80);
    sheet.heading("#0", text=colNames[0])
    sheet["columns"] = colNames[1:]
    for colName in colNames[1:]:
        sheet.column(colName, width=80);
        sheet.heading(colName, text=colName)

    for row in rows:
        sheet.insert('', 'end', text=row[0], values=row[1:])
    sheet.bind('<Double-1>', sheetDblClick)


    return

def sheetDblClick(event):
    global variable, fullFrame, sheet, rows, window2

    item = sheet.identify('item', event.x, event.y)  # 'I001' ....
    entNum = int(item[1:]) - 1  ## 쿼리한 결과 리스트의 순번
    id = rows[entNum][0]  ## 선택한 id
    window2.destroy()
    # DB에서 이미지를 다운로드
    obj = Search.Searching()
    con, cur = obj.getDBcon()

    sql = "SELECT fName, image FROM imageTBL WHERE id=" + str(id)  # ID로 이미지 추출하기
    cur.execute(sql)
    row = cur.fetchone()
    cur.close()
    con.close()
    # 임시 폴더
    fname, binData = row
    fullPath = tempfile.gettempdir() + '/' + fname  # 임시경로 + 파일명
    fp = open(fullPath, 'wb')  # 폴더를 지정.
    fp.write(binData)
    fp.close()

    if fname.split('.')[1].upper() != 'RAW':
        messagebox.showinfo('못봄', fname + '은 못봐요.ㅠㅠ')
        return

    return

def menuAddStyleBook():
    ######## MENU 5. 스타일 북 ########
    global variable, fullFrame, sheet, rows, window2

    if fullFrame != None:
        fullFrame.destroy()

    fullFrame = Frame(window);
    fullFrame.pack()


    pass


######## Main Menu   ########
mainMenu = Menu(window)
window.config(menu=mainMenu)

## Status Bar 추가
status = Label(window, text='이미지 정보:', bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

######## MENU 1. 검색 ########
searchMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "검색", menu=searchMenu)

searchMenu.add_cascade(label="옷장 검색", command=menuSearch1)

######## MENU 2. 추가 ########
addMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "추가", menu=addMenu)

addMenu.add_cascade(label="옷 추가하기", command=menuAdd1)

######## MENU 3. 옷 정보 검색 ########
clothsMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "옷 정보", menu=clothsMenu)

clothsMenu.add_cascade(label="가격 정보 검색", command=menuPrice)
clothsMenu.add_cascade(label="최근 착용일 검색", command=menuRecent)

######## MENU 4. 스타일링 ########
styleMenu = Menu(mainMenu)

sMenu=Menu(styleMenu)

mainMenu.add_cascade(label = "스타일링", menu=styleMenu)
styleMenu.add_cascade(label="action", menu=sMenu, command=None)
sMenu.add_cascade(label = "스타일링", command=None)
sMenu.add_cascade(label = "옷 색상 바꾸기", command=None)

######## MENU 5. 스타일 북 ########
styleBookMenu = Menu(mainMenu)

addStyleMenu=Menu(styleBookMenu)

mainMenu.add_cascade(label = "스타일 북", menu=styleBookMenu)
styleBookMenu.add_cascade(label="추가하기", menu=addStyleMenu, command=menuAddStyleBook)
addStyleMenu.add_cascade(label ="필터1", command=None)
addStyleMenu.add_cascade(label ="필터2", command=None)

######## MENU 6. 프린트하기 ########
printMenu = Menu(mainMenu)

mainMenu.add_cascade(label="프린트하기", menu=printMenu)
printMenu.add_cascade(label="프린트하기", command=printM.printFile("test")) # filename 전달하기.

window.mainloop()