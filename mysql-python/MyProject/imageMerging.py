from tkinter.filedialog import askopenfilename
import numpy as np
import cv2
from tkinter import *

def addImage(imgfile1, imgfile2):
    img1 = cv2.imread(imgfile1, cv2.IMREAD_COLOR)
    img2 = cv2.imread(imgfile2, cv2.IMREAD_COLOR)

    # 두이미지의 크기를 같게 만들어 준다.
    width=img2.shape[1]
    height=img2.shape[0]
    img2=cv2.resize(img2,(int(width/10),int(height/10)))
    img1=cv2.resize(img1, (int(width/10),int(height/10)))

    # ## 원본 이미지 출력
    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)

    add_img1 = img1 + img2
    add_img2 = cv2.add(img1, img2)

    ## 합성 이미지 출력
    cv2.imshow('add_img1', add_img1)
    cv2.imshow('add(img1,img2)', add_img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def  openImage() :
    global window, canvas, paper, inW, inH, outW, outH, inImageR, inImageG, inImageB, outImageR, outImageG, outImageB, filename
    filename1 = askopenfilename(parent=window, filetypes=(("영상 파일", "*.gif;*.jpg;*.png;*.bmp;*.tif"), ("모든 파일", "*.*")))
    print(filename1)
    if filename1 == "" or filename1 == None :
        return

    filename2 = askopenfilename(parent=window, filetypes=(("영상 파일", "*.gif;*.jpg;*.png;*.bmp;*.tif"), ("모든 파일", "*.*")))
    print(filename2)
    if filename2 == "" or filename2 == None:
        return


    addImage(filename1, filename2)

window=Tk()
openImage()