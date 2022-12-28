import cv2
image = cv2.imread(filename= r'C:\Users\sd63481\Desktop\image1_1.jpeg')

point1 = (150,200)#(width*height)
point2 = (300,400)#(width*height)
#BGR format
color = (155,169,37)
thick=5
image2 = cv2.line(img=image,pt1=point1,pt2=point2,color=color,thickness=thick,lineType=cv2.LINE_8)

image3 = cv2.arrowedLine(img=image,pt1=point1,pt2=point2,color=color,thickness=thick,tipLength=0.5)

#displaying the image
cv2.imshow('my_pic',image)
cv2.imshow('my_pic',image2)
cv2.waitKey(0)
cv2.destroyAllWindows()