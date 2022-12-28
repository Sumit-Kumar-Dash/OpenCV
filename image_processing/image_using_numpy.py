import cv2
from cv2 import pyrUp
import numpy as np


image = np.zeros((200,200))#grayscale image , 0-> black , other = white
cv2.rectangle(image,pt1=(0,100),pt2=(200,200),color=(30),thickness=-1)
cv2.rectangle(image,pt1=(50,80),pt2=(100,150),color=(1),thickness=-1)

cv2.imshow('pic',image)
cv2.waitKey(0)
cv2.destroyAllWindows()