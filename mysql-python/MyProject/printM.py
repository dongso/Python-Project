import os
from tkinter.filedialog import askopenfilename
from tkinter import *

def printFile():
    window=Tk()
    filename = askopenfilename(parent=window, filetypes=(("영상 파일", "*.gif;*.jpg;*.png;*.bmp;*.tif"), ("모든 파일", "*.*")))
    if filename == "" or filename == None:
        return
    print("printFile")
    os.startfile(filename, "print")