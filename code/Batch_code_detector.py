from picamera import PiCamera
from time import sleep
import numpy as np
import argparse
import cv2
import os
import RPi.GPIO as GPIO
import timeit

camera = PiCamera()
ir = 23
relay = 8
red = 10
green = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ir, GPIO.IN)
GPIO.setup(relay, GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(red, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(green, GPIO.OUT,initial=GPIO.HIGH)
start = timeit.default_timer()
while True:
 sensor = GPIO.input(ir)
 #sensor  = 0
 if sensor == 1:
  print("No")
  sleep(0.1)
 elif sensor == 0:
  print("Yes")
  # for n in range(1):
  # resize(width, height)
  n = 1
  camera.capture("snapshotnew_{:d}.jpg".format(n), resize=(640, 480))
  image = cv2.imread('snapshotnew_1.jpg')
  cv2.imshow("Original", image)
  cv2.waitKey(0)
  # ap = argparse.ArgumentParser("Desciption: ")
  # ap.add_argument("-i","--image", required = True, help = "Provide path to the image")
  # b = vars(ap.parse_args())

  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  cv2.imshow("Gray", gray)
  cv2.waitKey(0)

  blurred = cv2.GaussianBlur(gray,(1,1),0) # blur with standard deviation sigma = 9
  cv2.imshow("Blurred",blurred)
  cv2.waitKey(0)

  edge = cv2.Canny(blurred,10,30) # below 30 non edges and above 150 are sure edge
  cv2.imshow("Canny_edged",edge)
  cv2.waitKey(0)

  cropped = edge[350:490, 390:650]
  cv2.imshow("ROI", cropped)
  cv2.waitKey(0)
  (_,cnts,_) = cv2.findContours(cropped.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  crop = image[350:490, 390:650]
  cv2.imshow("ROI", crop)
  cv2.waitKey(0)

  print("I count {} countours in the image".format(len(cnts)))
  coins = crop.copy()

  for i in range(0,len(cnts)):
   area = cv2.contourArea(cnts[i])
   if (area>500):
    cv2.drawContours(coins,cnts,i,(0,255,0),1)
    cv2.imshow("Coins",coins)
    print(area)
    cv2.waitKey(0)
    (x, y, w, h) = cv2.boundingRect(cnts[i])
    a = x+390 - 224
    b = y+350 - 120
    c = a+165
    d = b+102
    print(x+390 - 224) #455
    print(y+350 - 120) #387
    print(c)
    print(d)
    ROI = edge[b:d, a:c]
    cv2.imshow("ROI", ROI)
    cv2.waitKey(0)
    path = '/home/pi'
    cv2.imwrite(os.path.join(path , 'crop1.jpg'), ROI)

    new = cv2.imread("crop1.jpg")
    new1 = cv2.cvtColor(new, cv2.COLOR_BGR2GRAY)
    height, width = new1.shape[:2]
    tu = []
    k = 0
    l = 0
    for k in range(height):
      for l in range(width):
          tu.append(new1[k, l])
    f = sum(tu)
    e = sum(tu[0:1148])
    if (e > 87000):
      new2 = edge[b + 10:d + 10, a:c]
      cv2.imshow("New2", new2)
      cv2.waitKey(0)
      path = '/home/pi'
      cv2.imwrite(os.path.join(path, 'crop2.jpg'), new2)
      new2 = cv2.imread("crop2.jpg")
      new3 = cv2.cvtColor(new2, cv2.COLOR_BGR2GRAY)
      height, width = new3.shape[:2]
      tu1 = []
      m = 0
      n = 0
      print(height - 1)
      for m in range(height):
          for n in range(width):
              tu1.append(new3[m, n])
      g = sum(tu1)
      print("The length of tuple: " + str(len(tu1)))
      print("The sum of values of tuple: " + str(g))
      if (g > 300000):
          print("Batch code is good, don't trigger!!")
          break
      else:
          print("No batch code or batch code is out of border. Please trigger!!")
          GPIO.output(green, GPIO.LOW)  # Turn on
          sleep(1)  # Sleep for 1 second
          GPIO.output(relay,GPIO.LOW)
          sleep(1)
          GPIO.output(relay,GPIO.HIGH)
          sleep(1)
          GPIO.output(red, GPIO.HIGH)  # Turn off
          sleep(5)
          GPIO.output(red, GPIO.LOW)  # Turn off
          sleep(1)
          GPIO.output(green, GPIO.HIGH)  # Turn on
          sleep(1)
          break
    elif (e > 70000):
      new4 = edge[b + 5:d + 5, a:c]
      cv2.imshow("New2", new4)
      cv2.waitKey(0)
      path = '/home/pi'
      cv2.imwrite(os.path.join(path, 'crop51.jpg'), new4)
      new5 = cv2.imread("crop51.jpg")
      new6 = cv2.cvtColor(new5, cv2.COLOR_BGR2GRAY)
      height, width = new6.shape[:2]
      tu2 = []
      i = 0
      j = 0
      print(height - 1)
      for i in range(height):
          for j in range(width):
              tu2.append(new6[i, j])
      h = sum(tu2)
      print("The length of tuple: " + str(len(tu2)))
      print("The sum of values of tuple: " + str(h))
      if (h > 300000):
          print("Batch code is good, don't trigger!!")
          break
      else:
          print("No batch code or batch code is out of border. Please trigger!!")
          GPIO.output(green, GPIO.LOW)  # Turn on
          sleep(1)  # Sleep for 1 second
          GPIO.output(relay, GPIO.LOW)
          sleep(1)
          GPIO.output(relay, GPIO.HIGH)
          sleep(1)
          GPIO.output(red, GPIO.HIGH)  # Turn off
          sleep(5)
          GPIO.output(red, GPIO.LOW)  # Turn off
          sleep(1)
          GPIO.output(green, GPIO.HIGH)  # Turn on
          sleep(1)
          break
    else:
     print("The length of tuple: " + str(len(tu)))
     print("The sum of values of tuple: " + str(sum(tu)))
     print("Th sum of first three row of image: " + str(e))
     if (f > 300000):
          print("Batch code is good, don't trigger!!")
          break
     else:
          print("No batch code or batch code is out of border. Please trigger!!")
          GPIO.output(green, GPIO.LOW)  # Turn on
          sleep(1)  # Sleep for 1 second
          GPIO.output(relay, GPIO.LOW)
          sleep(1)
          GPIO.output(relay, GPIO.HIGH)
          sleep(1)
          GPIO.output(red, GPIO.HIGH)  # Turn off
          sleep(5)
          GPIO.output(red, GPIO.LOW)  # Turn off
          sleep(1)
          GPIO.output(green, GPIO.HIGH)  # Turn on
          sleep(1)
          break
  cv2.destroyAllWindows()
