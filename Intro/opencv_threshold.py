import cv2
image = cv2.imread("image.jpg")
image = cv2.resize(image,dsize=(0,0),fx=0.5,fy=0.6)
ret,thresh = cv2.threshold(src=image,thresh = 100,maxval=255,type=cv2.THRESH_TOZERO_INV)


#THRESH_BINARY => pixel >=threhold =255:0
#THRESH_BINARY_INV => PIXEL >= THRESHOLD = 0:255
#TRESH_TRUNC =>       PIXEL >= THRESHOLD = THRESHOLD_VALUE:
#THRESH_TOZERO =>     PIXEL <= THRESHOLD = 0:PIXEL
#THRESH_TOZERO =>     PIXEL <= THRESHOLD = 0:PIXEL
#THRESH_TOZERO_INV =>     PIXEL >= THRESHOLD = 0:PIXEL

cv2.imshow('my_pic',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()