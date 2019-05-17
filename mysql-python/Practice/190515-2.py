import pymysql
from tkinter import *


## Global Variables ##
con = None  # connection
cur = None  # cursor
sql = ""  # query string
row = None  # 읽어들인 행 한개
host = "192.168.111.141"
user = "root"
pw = "1234"  # MySQL password


## Function Define ##

def insertData():
    # 1 데이터 베이스 연결
    con = pymysql.connect(host=host, user=user, password=pw, db='naverDB', charset='utf8')
    # 2. 커서 오픈
    cur = con.cursor()

    id = edt1.get()
    uname = edt2.get()
    uemail=edt3.get()
    uBorn = edt4.get()

    sql = "insert into naverTBL values('"+id+"','"+uname+"','"+uemail+"',"+uBorn+")"

    print(sql)
    cur.execute(sql)

    cur.close()
    con.commit()
    con.close()


def selectData():
    # 1 데이터 베이스 연결
    con = pymysql.connect(host=host, user=user, password=pw, db='naverDB', charset='utf8')
    # 2. 커서 오픈
    cur = con.cursor()

    sql = " SELECT id, uname, email, bornYear from naverTBL"
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
    cur.close()
    con.close()


## main ##
if __name__ == "__main__":
    window = Tk()
    window.geometry("600x300")
    window.title("GUI 데이터 입력")

    edtFrame = Frame(window)
    edtFrame.pack()

    listFrame = Frame(window)
    listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

    edt1 = Entry(edtFrame, width=10)
    edt1.pack(side=LEFT, padx=10, pady=10)

    edt2 = Entry(edtFrame, width=10)
    edt2.pack(side=LEFT, padx=10, pady=10)

    edt3 = Entry(edtFrame, width=10)
    edt3.pack(side=LEFT, padx=10, pady=10)

    edt4 = Entry(edtFrame, width=10)
    edt4.pack(side=LEFT, padx=10, pady=10)

    btnInsert = Button(edtFrame, text="입력", command=insertData)
    btnInsert.pack(side=LEFT, padx=10, pady=10)

    btnSelect = Button(edtFrame, text="조회", command=selectData)
    btnSelect.pack(side=LEFT, padx=10, pady=10)

    listData1 = Listbox(listFrame, bg='yellow')
    listData1.pack(side=LEFT, fill=BOTH, expand=1)

    listData2 = Listbox(listFrame, bg='yellow')
    listData2.pack(side=LEFT, fill=BOTH, expand=1)

    listData3 = Listbox(listFrame, bg='yellow')
    listData3.pack(side=LEFT, fill=BOTH, expand=1)

    listData4 = Listbox(listFrame, bg='yellow')
    listData4.pack(side=LEFT, fill=BOTH, expand=1)

    window.mainloop()



