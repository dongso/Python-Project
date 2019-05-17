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

def btnOpen():
    #사진 열기 ( 완성 못함)
    # 1 데이터 베이스 연결
    con = pymysql.connect(host=host, user=user, password=pw, db='animalsDb', charset='utf8')
    # 2. 커서 오픈
    cur = con.cursor()

    filename = ent1.get()
    sql = "SELECT photo FROM animalsTBL WHERE idx=13"
    messagebox.showinfo("sql", sql)

    cur.execute(sql)
    imageList=[]

    while True:
        row = cur.fetchone()
        if row == None or row == "":
            break
        imageList.append(row[0])



    for image in imageList:
        label1.insert(END, image=image)

    cur.close()
    con.commit()
    con.close()

#shutil.copy("C:/Pet_GIF", "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads")

window=Tk()
window.geometry("300x400")


def callback(e):
    img2 = ImageTk.PhotoImage(Image.open(path2))
    panel.configure(image=img2)
    panel.image = img2


ent1 = Entry(window, width=40); ent1.pack()
btn1 = Button(window, text="파일 불러오기", command=btnClick); btn1.pack()

ent2 = Entry(window, width=40); ent2.pack()
btn2 = Button(window, text="open", command=btnOpen); btn2.pack()
listFrame = Frame(window)
listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

# 사진 출력
label1 = Label(listFrame)
label1.pack(side=LEFT, fill=BOTH, expand=1)


img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

window.mainloop()