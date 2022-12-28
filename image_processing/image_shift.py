import cv2
import numpy as np

image = cv2.imread(filename= r'image.jpg')
image = cv2.resize(src=image,dsize=(0,0),fx=0.3,fy=0.3)
#print(image.shape)
height = image.shape[0]
width = image.shape[1]
dsize = (width,height)

#shift the image by (x,y) : [[1,0,x] , [0,1,y]]
M = np.float32([[1,0,100],[0,1,200]])
shifting = cv2.warpAffine(src=image,M=M,dsize=(width,height))

# cv2.imshow('pic',image)
# cv2.imshow('mask',shifting)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


l = [
  [   1, 3 ], # bottom-right
  [  3, 1 ], # top-right
  [  2, 2 ], # top-left
  [ 4, 3 ]  # bottom-left
]
print(sorted(l , key=lambda k: [k[1], k[0]]))