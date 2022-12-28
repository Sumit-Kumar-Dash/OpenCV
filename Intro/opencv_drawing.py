import cv2
image = cv2.imread(filename= r'C:\Users\sd63481\Desktop\image1_1.jpeg')
image = cv2.resize(src=image,dsize=(1000,1000))
def ellipse():
    center = (100,200)  #width*height
    axes = (100,50) #width*height
    start_angle = 0
    end_angle  = 360
    #try with start=90,end=180
    angle = 30 #rotation
    #BGR format
    color = (95,19,137)
    thick=5
    #thick=-1 , fill the circle with the color
    #lineType = for smoothness , LINE_AA -> (Anti alias)high smoothing . LINE_4 -> less smoothing
    image2 = cv2.ellipse(img=image,center=center,axes=axes,angle=angle,startAngle=start_angle,endAngle=end_angle
                    ,color=color,thickness=thick,lineType=cv2.LINE_AA)
    return image2

def rectangle():
    point1 = (150,200)#(width*height)
    point2 = (300,400)#(width*height)
    #BGR format
    color = (155,169,37)
    thick=5 #-1 will fill the rectangle
    image3 = cv2.rectangle(img=image,pt1=point1,pt2=point2,color=color,thickness=thick,lineType=cv2.LINE_8)
    return image3

def circle():
    center = (500,500)
    radius = 50
    #BGR format
    color = (95,19,137)
    thick=5
    #thick=-1 , fill the circle with the color
    #lineType = for smoothness , LINE_AA -> (Anti alias)high smoothing . LINE_4 -> less smoothing
    image4 = cv2.circle(img=image,center=center,radius=radius,color=color,thickness=thick,lineType=cv2.LINE_AA)
    return image4

def traingle():
    point1 = (0,70)#(width*height)
    point2 = (75,95)#(width*height)
    point3 = (180,10)#(width*height)
    #BGR format
    color = (155,169,37)
    thick=5
    cv2.line(img=image,pt1=point1,pt2=point2,color=color,thickness=thick)
    cv2.line(img=image,pt1=point2,pt2=point3,color=color,thickness=thick)
    cv2.line(img=image,pt1=point3,pt2=point1,color=color,thickness=thick)
    center_point = (((point1[0]+point1[0]+point3[0])//3),((point1[1]+point2[1]+point3[1])//3))
    print(center_point)
    #drawing center point of traingle
    cv2.circle(img=image,center=center_point,radius=1,color=color,thickness=thick,lineType=cv2.LINE_AA)

    #return(line1,line2,line3)

ellipse()
rectangle()
circle()
traingle()
#displaying the image
cv2.imshow('my_pic',image)
cv2.waitKey(0)
cv2.destroyAllWindows()