import pymysql
from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox

def btnClick() :
    filename=askopenfile(parent=window, filetypes=(("GIF파일", "*.gif"),("모든파일", "*.*")))
    ent1.insert(0, filename)
    #ent1.configure(text=str(filename))
    sql="insert into --- valeus(load_file('"+ent1.get()+"'))"
    messagebox.showinfo("sql",sql)


window = Tk()
window.geometry("300x400")

ent1 = Entry(window, width=50); ent1.pack()
btn1 = Button(window, text="파일 불러오기", command=btnClick); btn1.pack()



window.mainloop()