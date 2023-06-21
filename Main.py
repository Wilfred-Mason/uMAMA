import cv2
import numpy as np
import serial
import csv
import src.arduinoNano as arduinoNano
import src.camera as camera
import time
from datetime import datetime
import EditData


circleCentres = []

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        newClearFrame = clearFrame.copy()
        circleCentres.append(((x,y), 3))
        addFrame = camera.generateMask(newClearFrame, circleCentres)
        cv2.imshow("image", addFrame)
    if event == cv2.EVENT_RBUTTONDOWN:
        newClearFrame = clearFrame.copy()
        try:
            circleCentres.pop()
        except:
            print("No more circles left to remove!")
            pass
        subFrame = camera.generateMask(newClearFrame, circleCentres)
        cv2.imshow("image", subFrame)



if __name__ == "__main__":
    try:
        arduino = serial.Serial("COM5", 9600, timeout=0) #connect to arduino (change COM port if nessisary)
        arduinoNano.turnOffLight(arduino)
    except:
        print("ERROR!! Oopsies!! I think you forgot to connect the arduino! If the arduino is connected, hold your horses!! It may take a minute for the computer to detect the arduino")
        quit()

    uMAMA = input("Which uMAMA are you measuring? (input: integer 1 - 12): ")
    if (int(uMAMA) > 12 or int(uMAMA) < 1):
        print("That was an invalid input, you need to specify the uMAMA plate by an integer between 1 and 12")
        quit()

    print("working...")
    cam = cv2.VideoCapture(1) #initiate camera

    print("working...")

    arduinoNano.turnOnLight(arduino) #send signal to turn on backlight
    time.sleep(0.1)

    try:
        frame = camera.capture(cam)
        clearFrame = frame.copy()
    except:
        print("ERROR!!!!! Hmmm, make sure the camera is connected!! If the camera is connected, wait a tad bit longer, it may take a minute for the computer to detect the camera")
        quit()

    print("Select all of your sampling spots on the image using the left mouse click. To undo your last spot, use the right mouse click. When finished, click the 'Esc' key")
    cv2.imshow('image', frame)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)
    
    if len(circleCentres) != 16:
        print("Oh no! You didnt select 16 sampling spots. You need to run this program again :/")
        quit()

    circleCentres = camera.sortCircles(circleCentres)

    colours = camera.extractColour(clearFrame, circleCentres, uMAMA)

    EditData.addRow(uMAMA, colours)
    arduinoNano.turnOffLight(arduino)
    print("Data has been saved in 'uMAMA_"+ uMAMA + "/RGB_Data.csv' and image has been stored in 'uMAMA_"+uMAMA+"' folder")
