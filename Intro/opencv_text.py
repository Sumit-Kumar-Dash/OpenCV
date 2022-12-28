import cv2
image = cv2.imread(filename= r'C:\Users\sd63481\Desktop\image1_1.jpeg',flags=-1)
text1 = "Sumit Kumar Dash"
text2 = "Data Scientist"

#width*height
origin = (100,200)
origin2 = (300,400)
font = cv2.FONT_ITALIC
font_scale=2

#BGR
color = (100,143,39)
thickness = 3
line_type = cv2.LINE_AA

cv2.putText(img=image,text=text1,org=origin,fontFace=font,fontScale=font_scale,color=color,thickness=thickness)
cv2.putText(img=image,text=text2,org=origin2,fontFace=font,fontScale=font_scale,color=color,thickness=thickness)

cv2.imshow('my_pic',image)
cv2.waitKey(0)
cv2.destroyAllWindows()