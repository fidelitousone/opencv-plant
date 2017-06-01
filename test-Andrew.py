import cv2, time
import numpy as np
from matplotlib import pyplot as plt

#Canny Edge detection with noise filtering.
#(noise filtering currently commented out for testing on image with white background)
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

#This function creates the square around the plant and will also be used
#to get the height/width of the plant
def square(image,max_image_size):
    t0=time.time()
    x=0
    y=0
    minmax = [0,0,0,0]
    boundary = max_image_size - 1
    while True: #(top)
       #print x, y
       if image[x,y]==255: minmax[1] = y; break
       if(x < boundary) : x += 1
       else: x=0; y+=1

    x=boundary
    y=0
    while True: #(right)
        
       if image[x,y]==255: minmax[2] = x; break
       if(y < boundary) : y += 1
       else: y=0; x-=1

    x=0
    y=boundary
    while True: #(bottom)
       if image[x,y]==255: minmax[3] = y; break
       if(x < boundary) : x += 1
       else: x=0; y-=1

    x=0
    y=0
    while True: #(left)
       if image[x,y]==255: minmax[0] = x; break
       if(y < boundary) : y += 1
       else: y=0; x+=1
    t1= time.time()
    tf=t1-t0
    cv2.rectangle(image, (minmax[0], minmax[1]), (minmax[2],minmax[3]), (255,0,0),2)
    return minmax, tf

#loads image into program
img = cv2.imread('5plantDifferentS.png')
edges = cv2.Canny(img,100,100)  #Perform Canny Edge Detection

#Crop each individual plant
plant1 = edges[0:100, 0:100]
plant2 = edges[200:300, 0:100]
plant3 = edges[100:200, 100:200]
plant4 = edges[0:100, 200:300]
plant5 = edges[200:300, 200:300]

#Generate points for square and writes square to image.
#Returns square coordinates and time taken to perform function
print square(plant1, 100)
print square(plant2, 100)
print square(plant3, 100)
print square(plant4, 100)
print square(plant5, 100)

#Draws images to the screen in seperate windows
cv2.imshow("plant1", plant1)
cv2.imshow("plant2", plant2)
cv2.imshow("plant3", plant3)
cv2.imshow("plant4", plant4)
cv2.imshow("plant5", plant5)





#Press Q to close all windows (Necessary or program throws error)
if cv2.waitKey(1) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
cv2.waitKey(0)
cv2.destroyAllWindows()
