import pymysql
import mysql.connector
from tkinter import *

## Global variables
global host; host='192.168.111.128'
global user; user='machineUser'
global pw; pw='1234'

global con;
global cur;
global sql
global row

## Define Function3
def insertData():
    con = mysql.connector.connect(host=host, user=user, password=pw, db='machineDB', charset='utf8',auth_plugin='mysql_native_password')
    cur = con.cursor()

    id=edt1.get(); uname=edt2.get()
    sql="insert into machineTBL(id, uname) values("+id+", '"+uname+"')"
    #print(sql)
    cur.execute(sql)

    cur.close()
    con.commit()
    con.close()


def selectData():
    con = mysql.connector.connect(host=host, user=user, password=pw, db='machineDB', charset='utf8',auth_plugin='mysql_native_password')
    cur = con.cursor()

    sql="select id, uname from machineTBL"
    cur.execute(sql)

    idList=[]; nameList=[]
    while True:
        row=cur.fetchone()
        if row=="" or row ==None:
            break
        idList.append(row[0]); nameList.append(row[1])
    listData1.delete(0, listData1.size()-1); listData2.delete(0, listData2.size()-1)
    for id, name in zip(idList, nameList):
        listData1.insert(END, id); listData2.insert(END, name)

    cur.close()
    con.close()


## main
window = Tk(); window.geometry("600x300"); window.title("MySQL 연동(기본)")

edtFrame = Frame(window); edtFrame.pack()
listFrame = Frame(window); listFrame.pack(side=BOTTOM, fill = BOTH, expand=1)

edt1 = Entry(edtFrame, width=15); edt1.pack(side=LEFT, padx=10, pady=10)
edt2 = Entry(edtFrame, width=20); edt2.pack(side=LEFT, padx=10, pady=10)
btnInsert = Button(edtFrame, text="입력", command=insertData); btnInsert.pack(side=LEFT, padx=10, pady=10)
btnSelect = Button(edtFrame, text="조회", command=selectData); btnSelect.pack(side=LEFT, padx=10, pady=10)

listData1= Listbox(listFrame, bg='#F8C471' ); listData1.pack(side=LEFT, fill = BOTH, expand=1)
listData2 = Listbox(listFrame, bg='#D7BDE2'); listData2.pack(side=LEFT, fill = BOTH, expand=1)

window.mainloop()