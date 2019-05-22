from tkinter import messagebox

import pymysql
from tkinter.filedialog import *
import os.path
import tempfile
'''
    모든 바이너리 파일을 DB에 업로드 하는 프로그램
    ip : 192.168.111.141
    DBMS : linux, mysql 5.7
    DB : machinedb
    table : machinetbl (id, fName, fType, image)
     
'''
IP_ADDR = '192.168.111.141'
DB_NAME='machinedb'
TBL_NAME='machinetbl'
USER_NAME='root'
USER_PASS='1234'

## Global Variables
# global host; host='192.168.111.141'
# global user; user='machineUser'
# global pw; pw='P@ssw0rd'

global con,cur, sql, row

## Define Function3
def insertData():
    #파일 업로드

    con = pymysql.connect(host=IP_ADDR, user=USER_NAME, password=USER_PASS, db=DB_NAME, charset='utf8')
    cur = con.cursor()

    ## 파일 내용을 읽어오기
# step1. file open
    fp=open(edt1.get(),'rb')

#step2. file read
    bigData=fp.read()

# step3. file close
    fp.close()
    # step4. get file name
    fname = os.path.basename(edt1.get())
    fType = fname.split('.')[1]  # 파일 확장명 추출
    ## 쿼리 실행
    sql = "insert into machinetbl(fname,fType, image) values( %s, %s , %s)"
    tupleData = (fname, fType, bigData)
    cur.execute(sql, tupleData)

    cur.close()
    con.commit()
    con.close()


def fileDownload():
    # 파일 다운로드
    con = pymysql.connect(host=IP_ADDR, user=USER_NAME, password=USER_PASS, db=DB_NAME, charset='utf8')
    cur = con.cursor()


    sql="select id,fname, fType, image from machinetbl where id="+edt2.get()
    cur.execute(sql)

    ## Handling Exeption
    try:
        id, fName,fType, bigData = cur.fetchone()
    except:
        messagebox.showinfo('메시지', '파일이 존재하지 않습니다.')
        return

#step 1. '임시 폴더/파일명' 지정
    fullPath=tempfile.gettempdir()+'/'+fName
#step 2. file open
    fp=open(fullPath,'wb')
#step 3. Write file(save file)
    fp.write(bigData)
#step 4. Close file
    fp.close


    cur.close()
    con.commit()
    con.close()

    ##그림 보기

    messagebox.showinfo('완료', fullPath+'에 다운로드됨')

    photo=PhotoImage(file=fullPath)
    pLabel.configure(image=photo)
    pLabel.image=photo

def fileSelect():
    # 파일 선택
    edt1.delete(0,len(edt1.get()))
    filename = askopenfilename(parent=window, filetypes=(('이진 파일', '*.*'), ('모든 파일', '*.*')))
    edt1.insert(0, str(filename))


## Main ##
window = Tk(); window.geometry('700x200');  window.title('이진 파일 DB업로드')

# 업로드용 프레임
upFrame = Frame(window); upFrame.pack()
edt1 = Entry (upFrame, width=50); edt1.pack(side=LEFT, padx = 10, pady = 10)
btnFile = Button(upFrame, text="파일선택", command=fileSelect); btnFile.pack(side=LEFT, padx = 10, pady = 10)
btnUpload = Button(upFrame, text="업로드", command=insertData); btnUpload.pack(side=LEFT, padx = 10, pady = 10)

# 다운로드용 프레임
downFrame = Frame(window); downFrame.pack()
edt2 = Entry (downFrame, width=10); edt2.pack(side=LEFT, padx = 10, pady = 10)
btndownload = Button(downFrame, text="다운로드", command=fileDownload); btndownload.pack(side=LEFT, padx = 10, pady = 10)

# 그림 출력용
imageFrame = Frame(window); imageFrame.pack(side=BOTTOM, padx = 10, pady = 10)
photo=PhotoImage(); pLabel = Label(imageFrame, image=photo); pLabel.pack(expand=1, anchor=CENTER)


window.mainloop()