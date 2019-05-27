import numpy
import cv2
import scipy


### 1. 영상을 읽고 화면에 출력하고 싶어요. (gif 못 읽음)
# cvPhoto =  cv2.imread("C:\images\Pet_PNG\Pet_PNG(512x512)\cat02_512.png")
# #print(cvPhoto)
# cv2.imshow("TITLE", cvPhoto)
# cv2.waitKey()


# ### 2. 이미지를 GrayScale로 읽기
# cvPhoto =  cv2.imread("C:\images\Pet_PNG\Pet_PNG(512x512)\cat02_512.png", cv2.IMREAD_GRAYSCALE)
# #print(cvPhoto)
# cv2.imshow("TITLE", cvPhoto)
# cv2.waitKey()


### 3. 영상의 컬러 공간을 변화시킬수 있음.
oriPhoto =  cv2.imread("C:\images\Pet_PNG\Pet_PNG(512x512)\cat02_512.png")
# ## 3-1 : GrayScale로 변환
# grayPhoto = cv2.cvtColor(oriPhoto, cv2.COLOR_BGR2GRAY)
#
# #print(cvPhoto)
# cv2.imshow("Original", oriPhoto)
# cv2.imshow("Gray Sacle", grayPhoto)
# cv2.waitKey()

## 3-2 : YUV로 변환 -> Y: 밝기, U/V: 컬러 정보
# cvtPhoto=cv2.cvtColor(oriPhoto, cv2.COLOR_BGR2YUV)
# cv2.imshow("Original", oriPhoto)
# cv2.imshow("Y ", cvtPhoto[:,:,0])
# cv2.imshow("U ", cvtPhoto[:,:,1])
# cv2.imshow("V ", cvtPhoto[:,:,2])
# cv2.waitKey()


## 3-3 : HSV로 변환 --> H: 색조, S: 채도, V : 명도
# cvtPhoto=cv2.cvtColor(oriPhoto, cv2.COLOR_BGR2HSV)
# cv2.imshow("Original", oriPhoto)
# cv2.imshow("H ", cvtPhoto[:,:,0])
# cv2.imshow("S ", cvtPhoto[:,:,1])
# cv2.imshow("V ", cvtPhoto[:,:,2])
# cv2.waitKey()


## 3-4
cvtPhoto=cv2.cvtColor(oriPhoto, cv2.COLOR_BGR2HSV)
cv2.imshow("Original", oriPhoto)
cv2.imshow("H ", cvtPhoto[:,:,0])
cv2.imshow("S ", cvtPhoto[:,:,1])
cv2.imshow("V ", cvtPhoto[:,:,2])
cv2.waitKey()
