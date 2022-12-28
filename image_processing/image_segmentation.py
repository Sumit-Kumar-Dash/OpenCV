import cv2
import numpy as np

image = cv2.imread(filename= r'image.jpg')
image = cv2.resize(src=image,dsize=(0,0),fx=0.3,fy=0.3)

color_bgr = np.uint8([[[255,0,0]]]) # BGR
color_hsv = cv2.cvtColor(src=color_bgr,code = cv2.COLOR_BGR2HSV)
print(color_hsv)
#hsv_blue = (120,255,255) HSV

hsv = cv2.cvtColor(src=image,code = cv2.COLOR_BGR2HSV)

lower_blue = np.array([70,40,100])
higher_blue = np.array([160,255,255])

mask = cv2.inRange(src=hsv,lowerb=lower_blue,upperb=higher_blue)
#bitwise_and operation on image with itself(src1=image,src2=image) with mask 
result = cv2.bitwise_and(image,image,mask=mask)

cv2.imshow('pic',image)
cv2.imshow('mask',mask)
cv2.imshow('result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()