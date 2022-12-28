import cv2
image1 = cv2.imread(r'C:\Users\sd63481\Desktop\image2_1.png')
print(image1.shape)
image2 = cv2.imread(r'C:\Users\sd63481\Desktop\image1_1.png')
print(image2.shape)

image2 = cv2.resize(image2,dsize=(1864,7692))
print(image2.shape)

image3 = cv2.add(src1=image1,src2=image2)
print(image3)

image4 = cv2.subtract(src1=image1,src2=image2)
print(image4)

image5 = cv2.multiply(src1=image1,src2=image2)
print(image5)

image6 = cv2.divide(src1=image1,src2=image2)
print(image6)

#pixel range is [0,255]
#after add,subtract,multiply,divide : 
# if pixel value < 0 , it get rounded to zero
#                  >255 , it get rounded to 255
#               is in decimal : it get rounded to next value if decimal value >= .5 or 
#                                      rounded to pvs value if decimal value < .5

#scaling
'''pixel_updated = pixel_current * scale
after multiplication or division of image , 
pixel value get multiplied by scaling factor before its get rounded to nearest number
Eg: image1 = [1 4 6] , image2 = [2 3 5] , scale=4
image3 = image1/image2 = [1/2 4/3 6/5]=[0.5 1.3 1.2]
image3*scaling = [0.5 1.3 1.2]*4 = [2 5.2 4.8] = [2 5 5] after rounding up
'''
image7 = cv2.divide(src1=image1,src2=image2,scale=100)
print(image7)
image7 = cv2.resize(image7,dsize=(0,0),fx=0.5,fy=0.6)


#Weight add of one image to other image
'''
alpha = percentage of 1st iamge
beta = percentage of 2nd image
gamma = amount of brihtness need to add or subtract from final image
'''
image8 = cv2.addWeighted(src1=image1,alpha=0.1,src2=image2,beta=0.2,gamma=100)
image8 = cv2.resize(image8,dsize=(0,0),fx=0.5,fy=0.6)

cv2.imshow('my_pic',image8)
cv2.waitKey(0)
cv2.destroyAllWindows()