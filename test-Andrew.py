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
    kernal2 = np.ones((6,6),np.uint8)
    opening = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN,kernal2)
    opening = cv2.dilate(opening, None)
    #cv2.imshow("opening", opening)

    #Detect edges from the final morphed img
    edges = cv2.Canny(opening,100,100)
    #Trying to add the overlay sides to the original image
    #dst = cv2.addWeighted(img,0.7,edges,0.3,0)
    #cv2.imshow("image", image)

    #ret,dst = cv2.threshold(edges,127,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("edges", edges)
    return edges

    
    
img = cv2.imread('5plantDifferentS.png')
edges = cv2.Canny(img,100,100)

plant1 = edges[0:100, 0:100]
plant2 = edges[200:300, 0:100]
plant3 = edges[0:100, 0:100]
plant4 = edges[0:100, 0:100]
plant5 = edges[0:100, 0:100]

#edges = plantEdge(img)
cv2.imshow("plant1", plant1)
cv2.imshow("plant2", plant2)
cv2.imshow("plant3", plant3)
cv2.imshow("plant4", plant4)
cv2.imshow("plant5", plant5)

#Press Q to close all windows
if cv2.waitKey(1) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
cv2.waitKey(0)
cv2.destroyAllWindows()
