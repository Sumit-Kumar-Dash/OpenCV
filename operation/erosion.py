#erosion->reducing noise (converting white(1) to black(0)-reducing white)
#dilation->reducing noise (increasing white)
import cv2
cv2.erode()
cv2.dilate()
cv2.morphologyEx(op=cv2.MORPH_CLOSE)
cv2.morphologyEx(op=cv2.MORPH_OPEN)