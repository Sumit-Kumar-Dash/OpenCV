import cv2
import numpy as np
image = cv2.imread(r'image2.jpg')
image = cv2.resize(src=image,dsize=(0,0),fx=0.3,fy=0.3)


kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(image,op=cv2.MORPH_OPEN,kernel=kernel,iterations=5)
closing = cv2.morphologyEx(image,op=cv2.MORPH_CLOSE,kernel=kernel,iterations=5)
dilation = cv2.morphologyEx(image,op=cv2.MORPH_DILATE,kernel=kernel,iterations=5)
erosion = cv2.morphologyEx(image,op=cv2.MORPH_ERODE,kernel=kernel,iterations=5)

#gardient = erosion - dilation
gradient = cv2.morphologyEx(image,op=cv2.MORPH_GRADIENT,kernel=kernel,iterations=5)

#top_hat = original_image - opening 
top_hat = cv2.morphologyEx(image,op=cv2.MORPH_TOPHAT,kernel=kernel,iterations=5)

#black_hat = original_image-closing
black_hat = cv2.morphologyEx(image,op=cv2.MORPH_BLACKHAT,kernel=kernel,iterations=5)


cv2.imshow('image',image)
cv2.imshow('opening',opening)
cv2.imshow('closing',closing)
cv2.imshow('erosion',erosion)
cv2.imshow('dilation',dilation)
cv2.imshow('gradient',gradient)
cv2.imshow('top_hat',top_hat)
cv2.imshow('black_hat',black_hat)

cv2.waitKey(0)
cv2.destroyAllWindows(0)    