import cv2, time
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



def square(image):
    y=0
    x=0
    boundary = [100,100]
    minmax = []
    t0=int(time.time())
    while y < boundary[1]-1:
        print x,y
        if (image[x,y]==255) and (not minmax):
            minmax = [x,y,x,y]
        elif (image[x,y]==255) and (minmax):
            if minmax[0] > x:
                minmax[0] = x
            elif minmax[2] < x:
                minmax[2] = x
            if minmax[1] > y:
                minmax[1] = y
            elif minmax[3] < y:
                minmax[3] = y

        if (x<boundary[0]-1):
            x+=1
        else:
            x=0
            y+=1
    t1 = int((time.time()))
    tf = t1 - t0
    cv2.rectangle(image, (minmax[0], minmax[1]), (minmax[2],minmax[3]), (255,0,0),2)
    return minmax, tf
            
def leftside(image):
    y = 0
    x = 0
    D = []

    while y<100:
        if image[x,y] == 255:
            #distance from left is x, add the distance to the list "D"
            D.append(x) 
            #move onto the next row
            x=0
            y+=1
        elif (image[x,y] == 0) and (x>=50):
            y+=1
            x=0

        x+=1

        if x==100:
            x=0
            y+=1
    minLeft = min(D)
    return minLeft #return point closest to the left side

def rightside(image):
    y = 0
    x = 99
    D = []

    while y<100:
        if image[x,y] == 255:
            d=100-x #Distance from right side
            D.append(d)
            #move onto the next row
            x=99
            y+=1
        elif (image[x,y] == 0) and (x<=50):
            y+=1
            x=99

        x-=1

        if x==100:
            x=99
            y+=1
    minRight = 100- min(D)

    return minRight #return point closest to the right side

def topside(image):
    x = 0
    y = 0
    D = []

    while x<100:
        if image[x,y] == 255:
            #distance from top is y, add the distance to the list "D"
            D.append(y) 
            #move onto the next row
            y=0
            x+=1
        elif (image[x,y] == 0) and (y>=50):
            x+=1
            y=0

        y+=1

        if y==100:
            y=0
            x+=1
    minTop = min(D)
    return minTop #return point closest to the top side

def botside(image):
    x = 0
    y = 99
    D = []

    while x<100:
        if image[x,y] == 255:
            d=100-y #Distance from bot side
            D.append(d)
            #move onto the next row
            y=99
            x+=1
        elif (image[x,y] == 0) and (y<=50):
            x+=1
            y=99

        y-=1

        if y==100:
            y=99
            x+=1
    minBot = 100- min(D)

    return minBot #return point closest to the bot side


    
    
img = cv2.imread('5plantDifferentS.png')
edges = cv2.Canny(img,100,100)

plant1 = edges[0:100, 0:100]
print square(plant1)


'''
plant2 = edges[200:300, 0:100]
plant3 = edges[100:200, 100:200]
plant4 = edges[0:100, 200:300]
plant5 = edges[200:300, 200:300]
'''
#edges = plantEdge(img)


cv2.imshow("plant1", plant1)
'''
cv2.imshow("plant2", plant2)

cv2.imshow("plant3", plant3)
cv2.imshow("plant4", plant4)
cv2.imshow("plant5", plant5)
'''
#Press Q to close all windows
if cv2.waitKey(1) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
cv2.waitKey(0)
cv2.destroyAllWindows()
