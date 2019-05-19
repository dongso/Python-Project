import pymssql
from tkinter import *
from tkinter.filedialog import *
from collections import Iterable
from tkinter import messagebox

## Global variables...

global db; db = "khy"
global host; host = "192.168.111.130"
global user; user = "root"
global password; password = "1234"

global con; con=pymssql.connect(server=host, user=user, password=password, database=db)
global cur; cur=con.cursor()



## function Definition...
def dbDisConnection():
    cur.close()
    con.commit()
    con.close()


def Day1():
    #p52의 [그림 3-1]을 구축하라. DB이름은 자기이름영문약자.

    sql = "create table user_info(id char(10) primary key , name char(20), addr varchar(100)) "
    cur.execute(sql)

    sql="insert into user_info values('jee','지운이','서울 은평구 중산동')"
    cur.execute(sql)

    sql="insert into user_info values('Han','한주연','인천 남구 주안동')"
    cur.execute(sql)

    sql="insert into user_info values('Sang','상길이','경기 성남시 분당구')"
    cur.execute(sql)


def Day2():
#employees 데이터베이스의 테이블을 이용해서 인덱스, 뷰, 스토어드 프로시저, 트리거를 생성하고 운영하기

    while True:
        row=cur.fetchone()
        if row == "" or row == None:
            break

        print(row[0], row[1])



def Day31Insert():
    # Text 기반 Data 입력
    while True:
        id = input("Id : ")

        if id == "" or id == None:
            # break point
            break

        name = input("Name : ")
        addr=input("Address : ")
        birth=input("Birth : ")
        sql="insert into user_info values('"+id+"','"+name+"','"+addr+"','"+birth+"')"
        cur.execute(sql)
        con.commit()


def Day31Select():
    # Text 기반 Data 조회
    sql =" SELECT id, name, addr, birth from user_info where id='khy'"
    cur.execute(sql)
    print("== id ==== name ===== addr ==== Born Year")
    while True:
        row = cur.fetchone()
        if row == None or row == "":
            break
        print(" {0:4s}    {1:10s}  {2:4s}  {3:4s}".format(row[0], row[1],row[2],row[3]))

def Day31():
    Day31Insert()
    Day31Select()

def Day32Insert():

    id = edt1.get()
    uname = edt2.get()
    uemail=edt3.get()
    uBorn = edt4.get()

    sql = "insert into user_info values('"+id+"','"+uname+"','"+uemail+"',"+uBorn+")"

    print(sql)
    cur.execute(sql)
    con.commit()


def Day32select():

    sql = " SELECT id, name, addr, birth from user_info"
    cur.execute(sql)
    idList = []
    unameList = []
    emailList=[]
    bornYList=[]
    while True:
        row = cur.fetchone()
        if row == None or row == "":
            break
        idList.append(row[0])
        unameList.append(row[1])
        emailList.append(row[2])
        bornYList.append(row[3])


    listData1.delete(0, listData1.size() - 1)
    listData2.delete(0, listData2.size() - 1)
    listData3.delete(0, listData3.size() - 1)
    listData4.delete(0, listData4.size() - 1)

    for id, uname, email, born in zip(idList, unameList, emailList, bornYList):
        listData1.insert(END, id)
        listData2.insert(END, uname)
        listData3.insert(END, email)
        listData4.insert(END, born)


def Day32():
# 파이썬 교재 p.423의 데이터베이스 및 테이블을 완성한다.
# 텍스트 기반으로 위의 테이블을 입력/조회하는 파이썬 코드를 작성한다.
# GUI기반으로 데이터를 입력/ 조회하는 파이썬 코드를 작성한다.
    global window;
    window = Tk()
    window.geometry("600x300")
    window.title("GUI 데이터 입력")

    global edtFrame;
    edtFrame = Frame(window)
    edtFrame.pack()

    global listFrame;
    listFrame = Frame(window)
    listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

    global edt1;
    edt1 = Entry(edtFrame, width=10)
    edt1.pack(side=LEFT, padx=10, pady=10)

    global edt2;
    edt2 = Entry(edtFrame, width=10)
    edt2.pack(side=LEFT, padx=10, pady=10)

    global edt3;
    edt3 = Entry(edtFrame, width=10)
    edt3.pack(side=LEFT, padx=10, pady=10)

    global edt4;
    edt4 = Entry(edtFrame, width=10)
    edt4.pack(side=LEFT, padx=10, pady=10)

    global btnInsert;
    btnInsert = Button(edtFrame, text="입력", command=Day32Insert)
    btnInsert.pack(side=LEFT, padx=10, pady=10)

    global btnSelect;
    btnSelect = Button(edtFrame, text="조회", command=Day32select)
    btnSelect.pack(side=LEFT, padx=10, pady=10)

    global listData1;
    listData1 = Listbox(listFrame, bg='yellow')
    listData1.pack(side=LEFT, fill=BOTH, expand=1)

    global listData2;
    listData2 = Listbox(listFrame, bg='yellow')
    listData2.pack(side=LEFT, fill=BOTH, expand=1)

    global listData3;
    listData3 = Listbox(listFrame, bg='yellow')
    listData3.pack(side=LEFT, fill=BOTH, expand=1)

    global listData4;
    listData4 = Listbox(listFrame, bg='yellow')
    listData4.pack(side=LEFT, fill=BOTH, expand=1)

    window.mainloop()

def day42in():
    # day4, 동물 사진 등록
    filename=askopenfilename(parent=window4, filetypes=(("GIF 파일","*.gif"),("모든 파일","*.*")))
    ent14.insert(0, filename)

    sql="insert into animalTBL(kind, sex, img) select'dog', 'f', BulkColumn from Openrowset(Bulk'"+filename+"', Single_Blob) as Image"
    messagebox.showinfo("sql", sql)
    cur.execute(sql)

    con.commit()

def day41in():
    # day4 구매내역 입력
    userID = edt52.get()
    prodName = edt62.get()
    pGroup = edt72.get()
    price = edt82.get()
    amount = edt92.get()

    sql = "insert into buytbl(userid, prodName, groupName, price, amount) values('" + userID + "','" + prodName + "','" + pGroup + "'," + price + "," + amount + ")"

    print(sql)
    cur.execute(sql)


    con.commit()



def day41select():
    # 구매 목록 조회

    userID = edt12.get()
    sql = "select b.prodName as '상품명', b.amount as '개수', (b.amount*b.price) as '총 결제 금액' from buytbl b where b.userid='" + userID + "'"
    print(sql)
    cur.execute(sql)
    prodNameList = []
    amountList = []
    priceList = []

    while True:
        row = cur.fetchone()
        if row == None or row == "":
            break
        prodNameList.append(row[0])
        amountList.append(row[1])
        priceList.append(row[2])

    listData12.delete(0, listData12.size() - 1)
    listData22.delete(0, listData22.size() - 1)
    listData32.delete(0, listData32.size() - 1)

    for pName, amount, price in zip(prodNameList, amountList, priceList):
        listData12.insert(END, pName)
        listData22.insert(END, amount)
        listData32.insert(END, price)


def Day41():
    #미션 2,3
    global window2; window2 = Tk()
    window2.geometry("600x300")
    window2.title("GUI 데이터 입력")

    # 조회 하고자 하는 아이디를 입력받는다.
    global edtFrame2; edtFrame2 = Frame(window2)
    edtFrame2.pack()

    # 구매한 제품의 정보(제품명, 수량, 총 구매 금액)을 출력한다.
    global listFrame2; listFrame2 = Frame(window2)
    listFrame2.pack(side=BOTTOM, fill=BOTH, expand=1)

    # 사용자의 아이디를 입력받는다.
    global edt12; edt12 = Entry(edtFrame2, width=10)
    edt12.pack(side=LEFT, padx=10, pady=10)

    global btnInsert2; btnInsert2 = Button(edtFrame2, text="구매내역조회", command=day41select)
    btnInsert2.pack(side=LEFT, padx=10, pady=10)

    # 제품 이름 출력
    global listData12; listData12= Listbox(listFrame2, bg='yellow')
    listData12.pack(side=LEFT, fill=BOTH, expand=1)

    # 제품 수량 출력
    global listData22; listData22 = Listbox(listFrame2, bg='yellow')
    listData22.pack(side=LEFT, fill=BOTH, expand=1)

    # 해당 제품 구입 가격 출력
    global listData32; listData32 = Listbox(listFrame2, bg='yellow')
    listData32.pack(side=LEFT, fill=BOTH, expand=1)

    global edtFrame22; edtFrame22 = Frame(window2)
    edtFrame22.pack()

    # 사용자 아이디 입력
    global edt52; edt52 = Entry(edtFrame22, width=10)
    edt52.pack(side=LEFT, padx=10, pady=10)

    # 제품명 입력
    global edt62; edt62 = Entry(edtFrame22, width=10)
    edt62.pack(side=LEFT, padx=10, pady=10)

    # 제품군 입력
    global edt72; edt72 = Entry(edtFrame22, width=10)
    edt72.pack(side=LEFT, padx=10, pady=10)

    # 제품 가격 입력
    global edt82; edt82 = Entry(edtFrame22, width=10)
    edt82.pack(side=LEFT, padx=10, pady=10)

    # 구매 개수 입력
    global edt92;edt92 = Entry(edtFrame22, width=10)
    edt92.pack(side=LEFT, padx=10, pady=10)

    global btnSelect2; btnSelect2 = Button(edtFrame22, text="구매", command=day41in)
    btnSelect2.pack(side=LEFT, padx=10, pady=10)

    window2.mainloop()

def Day42():
    #미션 1, 4, 5
    global window4; window4 = Tk()
    window4.geometry("300x400")

    global ent14; ent14 = Entry(window4, width=40);
    ent14.pack()
    global btn14; btn14 = Button(window4, text="파일 저장하기", command=day42in);
    btn14.pack()

    window4.mainloop()


## Start Main...

# Day1()
# Day2()
#Day31()
#Day32()
#Day41()
Day42()



dbDisConnection()

