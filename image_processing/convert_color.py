import cv2
image = cv2.imread(filename= r'C:\Users\sd63481\Desktop\image1_1.jpeg')
#converts an input image from one color space to another
image = cv2.cvtColor(src=image,code=cv2.COLOR_BGR2HSV)
cv2.imshow('my_pic',image)
cv2.waitKey(0)
cv2.destroyAllWindows()