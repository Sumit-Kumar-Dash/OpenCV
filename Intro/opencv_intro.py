'''
image is collection of pixels
image shape = width*height*channel , c=channel : 1=grey , 3=bgr ,4=bgr+alpha channel

BGR representation
white color = 255*255*255
black color = 0*0*0
blue color = 255*0*0
green color = 0*255*0
red color = 0*0*255

https://www.yangcha.github.io/ImageViewer/


HSV = Hue Saturation Value
Hue  range [0,360] . 
H = 0 =360 = Red 
H = 120 = Green
H = 240 = Blue

Saturation  range from [0,1] = how much gray /chroma
Saturation = 0 = very white
Saturation = 1 = very 

Value range from [0,1] = Brightness(Lightness)
value = 0 = light
value = 1 = dark

'''

import cv2

'''flag value :
to read image in color format which doesnot include alpha channel =1, cv2.IMREAD_COLOR
to read image in greyscale = 0, cv2.IMREAD_GREYSCALE
to read image as it including alpha channel=-1, cv2.IMREAD_UNCHANGED
flags works for .png , not for .jpg or .jpeg'''

#read the image
image = cv2.imread(filename= r'C:\Users\sd63481\Desktop\image1_1.jpeg',flags=-1)

print(f"Image is {image}")
print(f"1st row of pixel of image is{image[0]}")
print(image.shape)

#resizing the image
width = 400
height = 500
dimension = (width,height)
image2 = cv2.resize(src=image,dsize=dimension)
print(image2.shape)

#fx means width , 0.1 = 10% of original size
#fy means height , 0.4 = 40% of original size
image3 = cv2.resize(src=image,dsize=(0,0),fx=0.1,fy=0.2)


#save the image
cv2.imwrite(r'C:\Users\sd63481\Desktop\OpenCV\image1.png',image)

#displaying the image
cv2.imshow('my_pic',image3)

#waitkey=0 means it will destroy only when any key pressed 
# waitkey=10000 means it will destroy automatically after 10000 milisecond =10sec 
cv2.waitKey(0)
cv2.destroyAllWindows()