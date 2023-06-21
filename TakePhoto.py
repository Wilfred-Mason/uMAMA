import src.camera as camera
import cv2
from datetime import datetime

cam = cv2.VideoCapture(1)
uMAMA = input("Which uMAMA are you taking a photo of? (input: integer 1-12): ")
frame = camera.capture(cam)
print("Is this photo good? Click any keyboard key to continue to save photo")
cv2.imshow("photo", frame)
cv2.waitKey(0)
timePoint = datetime.now().strftime("%m-%d-%Y_%H-%M-%S")
cv2.imwrite("uMAMA_" + uMAMA + "/uMAMA_" + uMAMA + "_{0}.jpeg".format(timePoint), frame)
print("Image was saved")