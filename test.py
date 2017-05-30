import cv2
import numpy as np
from matplotlib import pyplot as plt

#Not used in this test (ROI - cropping)
#rows,cols,channels = img.shape
#plant1 = img[30:90, 0:70]
#plant2 = img[0:100, 100:210]

def plantEdge(image):
    #Read image and make it gray
    #img = cv2.imread(image)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #cv2.imshow("gray", gray)

    #Apply a binary threshold
    ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    #cv2.imshow("thresh1", thresh1)

    #apply opening morph to remove smaller noise
    #Using
    kernal2 = np.ones((6,6),np.uint8)
    opening = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN,kernal2)
    opening = cv2.dilate(opening, None)
    #cv2.imshow("opening", opening)
    #This is a test
	# This is programming stuff

    #Detect edges from the final morphed img
    edges = cv2.Canny(opening,800,800)
    #Trying to add the overlay sides to the original image
    #dst = cv2.addWeighted(img,0.7,edges,0.3,0)
    cv2.imshow("image", image)

    #ret,dst = cv2.threshold(edges,127,255,cv2.THRESH_BINARY_INV)
    cv2.imshow("edges", edges)

    #Press Q to close all windows
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img=cv2.imread('basilTop.jpg')

plantEdge(img)
