from timeit import default_timer as timer
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
pins = [1, 2, 3]
GPIO.setup(pins, GPIO.IN)

if GPIO.input(1):
	start = timer()

if GPIO.input(2):
	end = timer()

print(end - start)  
