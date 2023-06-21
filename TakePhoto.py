import src.camera as camera
import cv2
from datetime import datetime
import src.arduinoNano as arduinoNano
import serial
import time

try:
    arduino = serial.Serial(arduinoNano.COMPort, 9600, timeout=0) #connect to arduino (change COM port if nessisary)
    arduinoNano.turnOffLight(arduino)
except:
    print("ERROR!! Oopsies!! I think you forgot to connect the arduino! If the arduino is connected, hold your horses!! It may take a minute for the computer to detect the arduino")
    quit()

uMAMA = input("Which uMAMA are you taking a photo of? (input: integer 1 - 12): ")
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
except:
    print("ERROR!!!!! Hmmm, make sure the camera is connected!! If the camera is connected, wait a tad bit longer, it may take a minute for the computer to detect the camera")
    quit()

print("Is this photo good? Click the 'y' key to continue. Click the 'n' key to cancel")
cv2.imshow("photo", frame)
c = cv2.waitKey(0)

if c == 121:
    timePoint = datetime.now().strftime("%m-%d-%Y_%H-%M-%S")
    cv2.imwrite("uMAMA_" + uMAMA + "/uMAMA_" + uMAMA + "_{0}.jpeg".format(timePoint), frame)
    print("Image was saved")
else:
    print("Aborted. Run program again!")