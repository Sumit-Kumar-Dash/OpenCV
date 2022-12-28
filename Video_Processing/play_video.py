import cv2
cap = cv2.VideoCapture(r'C:\Users\sd63481\Desktop\OpenCV\Feature_Detection\Pexels Videos 2795172.mp4')
cnt = 0
while True:
    ret,frame = cap.read()
    cv2.resize(frame,dsize=(0,0),fx=0.3,fy=0.3)
    cv2.imshow('frame',frame)
    cv2.imwrite(fr'C:\Users\sd63481\Desktop\OpenCV\Video_Processing\imges\img_{cnt}.jpg',frame)
    cnt+=1

    if cv2.waitKey(25) & 0xFF==ord('q'):#1000 -> 1000ms=1sec

        cap.release()
        break
cv2.destroyAllWindows()