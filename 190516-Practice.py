from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter.filedialog import *
import shutil

## Global Variables ##
con = None  # connection
cur = None  # cursor
sql = ""  # query string
row = None  # 읽어들인 행 한개
host = "localhost"
user = "root"
pw = "1234"  # MySQL password

def btnClick():
    # 1 데이터 베이스 연결
    con = pymysql.connect(host=host, user=user, password=pw, db='animalsDb', charset='utf8')
    # 2. 커서 오픈
    cur = con.cursor()

    filename=askopenfilename(parent=window, filetypes=(("GIF 파일","*.gif"),("모든 파일","*.*")))
    ent1.insert(0, filename)
    sql="INSERT INTO animalsTBL(animalGroup, animalSex, photo) VALUES ('cat', 'm', LOAD_FILE('"+filename+"'))"
    messagebox.showinfo("sql", sql)

    cur.execute(sql)

    cur.close()
    con.commit()
    con.close()


#shutil.copy("C:/Pet_GIF", "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads")

window=Tk()
window.geometry("300x400")




ent1 = Entry(window, width=40); ent1.pack()
btn1 = Button(window, text="파일 불러오기", command=btnClick); btn1.pack()


window.mainloop()