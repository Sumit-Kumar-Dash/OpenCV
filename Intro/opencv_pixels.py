import cv2
image = cv2.imread(filename= r'C:\Users\sd63481\Desktop\image1_1.jpeg')

print(f"Image is {image}")
print(f"1st row of pixel of image is{image[0]}")
print(image.shape)

#making image as white for height=200,width=100
image[0:100,0:200]=[255,255,255]
print(image[0:100,0:100])

#making image as blue for height=100-200,width=200-300
image[200:300,100:200]=[135,42,42]
print(image[0:100,0:100])

#displaying the image
cv2.imshow('my_pic',image)
cv2.waitKey(0)
cv2.destroyAllWindows()