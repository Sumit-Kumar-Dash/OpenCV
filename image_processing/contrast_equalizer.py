import cv2
from cv2 import COLOR_BGR2YCrCb

#grey scale image
'''image = cv2.imread(r'image.jpg',flags=0)
image = cv2.resize(src=image,dsize=(0,0),fx=0.3,fy=0.3)
equ = cv2.equalizeHist(image)'''

#color image
image = cv2.imread(r'image.jpg',flags=1)
image = cv2.resize(src=image,dsize=(0,0),fx=0.3,fy=0.3)

new_image = cv2.cvtColor(image,cv2.COLOR_BGR2YCrCb)
#equalize the histogram of 3rd channel
new_image[:,:,0] = cv2.equalizeHist(new_image[:,:,0])
equ = cv2.cvtColor(new_image,cv2.COLOR_YCrCb2BGR)
#equ = cv2.equalizeHist(image[:,:,2])

cv2.imshow('image',image)
cv2.imshow('contrast equalizer',equ)
cv2.waitKey(0)
cv2.destroyAllWindows()