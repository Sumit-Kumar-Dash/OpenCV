import cv2
from matplotlib.scale import scale_factory
#step1 : loading the image and resizing as required
image = cv2.imread(r'C:\Users\sd63481\Desktop\OpenCV\image.jpg',1)
image = cv2.resize(src=image,dsize=(0,0),fx=0.3,fy=0.3)
#Step2: Converting the image to grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

'''algorithms for facial detection is “haarcascade”.
#It is computationally less expensive, a fast algorithm, and gives high accuracy'''

#Step3:Loading the required haar-cascade XML classifier file
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
#Step4:  Applying the face detection method on the grayscale image
faces = face_cascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=9)
'''you can change the value of minNeighbors to get more or small faces
    minNeighbors decide how much point to decide for the face'''
print(faces)
#Step 5: Iterating through rectangles of detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
    cv2.putText(img=image,text="Face",org=(x,y),
                fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=2,color=(0,255,255),thickness=2)
cv2.imshow('pic',image)
cv2.waitKey(0)
cv2.destroyAllWindows()