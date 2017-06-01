
def square(image):
    y=0
    x=0
    boundary = [100,100]
    minmax = []
    t0=int(time.time())
    while y < boundary[1]:
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

