import cv2
image = cv2.imread(r'C:\Users\sd63481\Desktop\OpenCV\image.jpg',1)
image = cv2.resize(src=image,dsize=(0,0),fx=0.7,fy=0.7)

#https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_smile.xml")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,scaleFactor=1.4,minNeighbors=9)
print(faces)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), thickness=2)
    cv2.putText(img=image,text="Face",org=(x,y),
                fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=2,color=(0,255,255),thickness=2)

    # to find out eyes only in those areas where face got detected
    roi_gray = gray[y:y+h,x:x+h]
    roi_color = image[y:y+h,x:x+h]

    eyes = eye_cascade.detectMultiScale(image=roi_gray,scaleFactor=1.2,minNeighbors=4)
    smile = smile_cascade.detectMultiScale(image=roi_gray,scaleFactor=1.2,minNeighbors=4)
    print("Sumit",eyes)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 55, 255), thickness=2)
        cv2.putText(img=roi_color,text="Eye",org=(ex,ey),
                 fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=2,color=(0,255,255),thickness=2)

    for (sx,sy,sw,sh) in smile:
        cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (55, 55, 255), thickness=2)
        cv2.putText(img=roi_color,text="Smile",org=(sx,sy),
                 fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=2,color=(0,255,255),thickness=2)

cv2.imshow('pic',image)
cv2.waitKey(0)
cv2.destroyAllWindows()


