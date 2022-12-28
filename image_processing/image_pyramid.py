import cv2
from cv2 import pyrUp
import numpy as np

image = cv2.imread(filename= r'image.jpg')
image = cv2.resize(src=image,dsize=(0,0),fx=0.3,fy=0.3)
print(image.shape)
height = image.shape[0]
width = image.shape[1]
dsize = (width,height)
for i in range(10):
    #image = cv2.pyrDown(image)
    image = cv2.pyrUp(image)
    print(image.shape)
    cv2.imshow('pic',image)
    #cv2.imshow('mask',down)
    cv2.waitKey(0)
cv2.destroyAllWindows()