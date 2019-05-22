import pymysql
from tkinter.filedialog import *
import os.path
import tempfile

## Global Variables
global host; host='192.168.111.141'
global user; user='machineUser'
global pw; pw='P@ssw0rd'

global con,cur, sql, row

## Define Function3
def insertData():
    #파일 업로드

    con = pymysql.connect(host=host, user=user, password=pw, db='machinedb', charset='utf8')
    cur = con.cursor()

    ## 파일 내용을 읽어오기
# step1. file open
    fp=open(edt1.get(),'rb')

#step2. file read
    bigData=fp.read()

# step3. file close
    fp.close()

# step4. get file name
    fname=os.path.basename(edt1.get())

    ## 쿼리 실행
    sql="insert into machinetbl(fname, image) values( %s, %s)"
    tupleData=(fname, bigData)
    cur.execute(sql,tupleData)


    cur.close()
    con.commit()
    con.close()


def fileDownload():
    # 파일 다운로드
    con = pymysql.connect(host=host, user=user, password=pw, db='machinedb', charset='utf8')
    cur = con.cursor()


    sql="select id,fname, image from machinetbl where id="+edt2.get()
    cur.execute(sql)

    id, fName, bigData = cur.fetchone()
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
    photo=PhotoImage(file=fullPath)
    pLabel.configure(image=photo)
    pLabel.image=photo

def fileSelect():
    # 파일 선택
    filename = askopenfilename(parent=window, filetypes=(('GIF 파일', '*.gif'), ('모든 파일', '*.*')))
    edt1.delete(0,'end')
    edt1.insert(0, str(filename))


## Main ##
window = Tk(); window.geometry('700x500');  window.title('MySQL 연동 대용량')

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