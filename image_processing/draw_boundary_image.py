import cv2
image = cv2.imread(filename= r'C:\Users\sd63481\Desktop\ca-20220610_001-1.jpg',flags=-1)
image = cv2.resize(src=image,dsize=(0,0),fx=0.5,fy=0.3)
iamge = cv2.copyMakeBorder(image,top=300,bottom=500,left=30,right=170,borderType=cv2.BORDER_REFLECT)
cv2.imshow('pic',iamge)
cv2.waitKey(0)
cv2.destroyAllWindows()
