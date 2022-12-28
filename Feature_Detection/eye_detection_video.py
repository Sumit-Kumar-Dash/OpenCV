import numpy as np
import cv2

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_smile.xml")

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.4,minNeighbors=3)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(img,text="Face",org=(x,y),
                 fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=2,color=(0,255,255),thickness=2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(image=roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            cv2.putText(img=roi_color,text="Eye",org=(ex,ey),
                 fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=2,color=(0,255,255),thickness=2)
        
        smile = smile_cascade.detectMultiScale(image=roi_gray,scaleFactor=1.2,minNeighbors=4)
        for (sx,sy,sw,sh) in smile:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (55, 55, 255), thickness=2)
            cv2.putText(img=roi_color,text="Smile",org=(sx,sy),
                    fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=2,color=(0,255,255),thickness=2)

    cv2.imshow('video',img)
    if cv2.waitKey(25) & 0xFF==ord('q'):#1000 -> 1000ms=1sec

        cap.release()
        break
cv2.destroyAllWindows()