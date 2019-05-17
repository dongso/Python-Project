from tkinter import *
from tkinter import messagebox


def myFunc():
    messagebox.showinfo("강아지 버튼", "강아지가 귀엽죠? ^^")



window = Tk()

label1 = Label(window, text="빅데이터 열공중...", bg="magenta", font=('궁서체',30), fg='blue')
window.geometry("300x400")
photo=PhotoImage(file='C:\images\Pet_GIF\Pet_GIF(256x256)\cat01_256.gif')

label2=Label(window, image=photo)



label1.pack()
label2.pack(expand=1,anchor=CENTER)

button1 = Button(window, text="파이썬 종료", fg='red', command=myFunc); button1.pack()

window.mainloop()

