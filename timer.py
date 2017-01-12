from timeit import default_timer as timer
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
pins = [3, 5, 3]
GPIO.setup(pins, GPIO.IN)
while 1:
	if GPIO.input(3):
		start = timer()
	if GPIO.input(5):
		end = timer()
		time.sleep(0.3)
		print(end - start)  
