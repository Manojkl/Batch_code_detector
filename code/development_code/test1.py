import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep

camera = PiCamera()
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(23, GPIO.IN)
sensor = 1
while True:
 #sensor = GPIO.input(23)
 if sensor == 1:
  print("No")
  sleep(0.1)
 elif sensor == 0:
  print("Yes")
  for n in range(3):
      sleep(3)
      camera.capture("snapshot12_{:d}.jpg".format(n), resize=(640, 480))
