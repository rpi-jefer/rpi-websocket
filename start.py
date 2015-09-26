import time
import RPi.GPIO as GPIO
GPIO.setup(22,GPIO.IN)
prev_input = 0
while True:
  input = GPIO.input(22)
  if ((not prev_input) and input):
    print("Button pressed")
    archivo = open('estado.txt','w')
    archivo.write('1')
  archivo.close()
  prev_input = input
  time.sleep(0.05)
