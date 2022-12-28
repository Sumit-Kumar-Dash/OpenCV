import cv2

cap = cv2.VideoCapture(0) 
#0-> real time inbuilt laptop camera , 1-> real time external camera feeded to laptop
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
#need to tune above parameters as image changes
while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
    print(faces)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
    cv2.imshow('video',frame)
    if cv2.waitKey(25) & 0xFF==ord('q'):#1000 -> 1000ms=1sec

        cap.release()
        break
cv2.destroyAllWindows()