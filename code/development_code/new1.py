import numpy as np
import cv2
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
import timeit


camera = PiCamera()
#camera.resolution = (800, 600)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(14, GPIO.OUT,initial=GPIO.LOW)
n=100
start = timeit.default_timer()
while True:
 sensor = GPIO.input(23)
 if sensor == 1:
  print("No")
  sleep(0.1)
 elif sensor == 0:
  print("Yes")
  #for n in range(1):
  #resize(width, height)
  camera.capture("snapshot15_{:d}.jpg".format(n), resize=(640, 480))
  n=n+1
  """image = cv2.imread('snapshot12_0.jpg')
  cv2.imshow("Original",image)
  cv2.waitKey(0) 
  #y:y+h, x:x+w
  cropped = image[200:330, 320:550]
  cv2.imshow("ROI", cropped)
  cv2.waitKey(0)
  gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
  cv2.imshow("Gray", gray)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  height, width = gray.shape[:2]
  tu = []
  i=0
  j=0
  #print(height-1)
  for i in range(height):
    for j in range(width):
     tu.append(gray[i,j])
  #if(sum(tu) >
  GPIO.output(14, GPIO.HIGH) # Turn on
  sleep(1)                  # Sleep for 1 second
  GPIO.output(14, GPIO.LOW)  # Turn off
  sleep(1)
  #print(tu)
  print(len(tu))  
  print(sum(tu))
  #break"""
stop = timeit.default_timer()
print('Time: ', stop - start)
