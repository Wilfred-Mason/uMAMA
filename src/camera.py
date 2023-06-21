import cv2
import numpy as np
from PIL import Image, ImageTk
from datetime import datetime

def set(camera, exposure, brightness, saturation, gain, contrast):
    camera.set(cv2.CAP_PROP_EXPOSURE, exposure)
    camera.set(cv2.CAP_PROP_BRIGHTNESS, 100)
    camera.set(cv2.CAP_PROP_SATURATION, saturation)
    camera.set(cv2.CAP_PROP_GAIN, gain)
    camera.set(cv2.CAP_PROP_CONTRAST, contrast)

def liveStream(camera):
    while True:
        ret, frame = camera.read()
        frame = frame[65:465, 125:525]
        cv2.imshow('Input', frame)

        c = cv2.waitKey(1)
        if c == 27: 
            break

def capture(camera):
    ret, frame = camera.read()
    frame = frame[110:335, 195:420]
    return frame

def detectCircles(frame, minRadius, blur):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, blur) 
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, (gray.shape[0])/8, param1=120, param2=60, minRadius= minRadius, maxRadius=150)
    return circles

def sortCircles(circles):
    sortedCircles = []
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    for circle in circles: 
        if (circle[0][1] < 50):
            row1.append(circle)
        elif (circle[0][1] > 50) and (circle[0][1] < 100):
            row2.append(circle)
        elif (circle[0][1] > 100) and (circle[0][1] < 170):
            row3.append(circle)
        elif (circle[0][1] > 170):
            row4.append(circle)
    row1 = sorted(row1, key = lambda x: x[0])
    row2 = sorted(row2, key = lambda x: x[0])
    row3 = sorted(row3, key = lambda x: x[0])
    row4 = sorted(row4, key = lambda x: x[0])
    sortedCircles = row1 + row2 + row3 + row4
    return sortedCircles

def generateMask(frame, circleCentres):
    for circle in circleCentres:
        frame = cv2.circle(frame, circle[0], 5, (0, 0,255), 1)       
    return frame

def numberCircles(maskedImage, sortedCircles):
    for i, circle in enumerate(sortedCircles):
        maskedImage = cv2.putText(maskedImage, str(i+1), (int(circle[0] + 20), int(circle[1] + 5)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    return maskedImage

def displayImage(image):
    print("If the sampling spots are in the correct spots, click 'y' when on the image tab. Click 'n' if the spots don't match and restart the program")
    while (True):
        cv2.imshow("window", image)
        c = cv2.waitKey(0)
        if c == 121:
            break
        else:
            print("Program closed. Try to move the uMAMA or the camera around to try to get the right sampling spots")
            quit()
            
def extractColour(frame, circleCentres, uMAMA):
    allCircleColours = []
    for centre in circleCentres:
            mask = np.zeros(frame.shape[:2], dtype="uint8")
            mask = cv2.circle(mask, centre[0], centre[1], (255, 255, 255), -1)
            maskedimages = cv2.bitwise_and(frame, frame, mask = mask)
            colour = list(cv2.mean(frame, mask))
            colour = colour[:-1]
            colour.reverse()
            allCircleColours = allCircleColours + colour
            timePoint = datetime.now().strftime("%m-%d-%Y_%H-%M-%S")
            cv2.imwrite("uMAMA_" + uMAMA + "/uMAMA_" + uMAMA + "_{0}.jpeg".format(timePoint), frame)
    allCircleColours.insert(0, timePoint)
    return allCircleColours
