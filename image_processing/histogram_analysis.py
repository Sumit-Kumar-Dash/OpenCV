import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(filename= r'image.jpg')
image = cv2.resize(src=image,dsize=(0,0),fx=0.3,fy=0.3)
print(image.shape)
#shape = (410,614,3) ,Total pixels = 410*614*3 =755220
#pixel min value =0 ,max=255
# histogram analyis is the analysis of pixel decomposition of B,G,R , count of pixels in range of (0,255)
'''plt.hist(image.ravel(),256,[0,256])
plt.hist(image[0].ravel(),256,[0,256]) #blue part
plt.hist(image[1].ravel(),256,[0,256]) #green part
plt.hist(image[2].ravel(),256,[0,256]) #red part
plt.show()'''

'''hist = cv2.calcHist(images=[image],channels=[0],mask=None,histSize=[256],ranges=[0,256])
plt.plot(hist)
plt.show()'''

b,g,r = cv2.split(image)
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])

cv2.imshow('b',b)
cv2.imshow('r',r)
cv2.imshow('g',g)

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()