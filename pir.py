#!/usr/bin/env python
#-- coding: utf-8 --

# Import necessary libraries
import RPi.GPIO as GPIO
import time, argparse


# Initialize variables
pin = None

# Get arguments
parser = argparse.ArgumentParser()

parser.add_argument("pin", type=int, help="The pin of the PIR sensor.")
parser.add_argument("bh1750", type=int, help="is a bh7150 present?")


args = parser.parse_args()

pin = args.pin
bh1750enabled = args.bh1750

if(bh1750enabled == 0):
	bh1750enabled = False
else:
	bh1750enabled = True

print("Config PIN:"+str(pin)+"| bh1750:"+str(bh1750enabled))

# Configure GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.IN)

# Indicate PIR sensor start
print("PIR_START")

# import bh1750 if enabled
if bh1750enabled:
	import bh1750

# Script
try:
	time.sleep(2) # Sensor Stabilization Delay (2 seconds)
	
	# Infinite loop
	while True:
		if GPIO.input(pin):
			print("USER_PRESENCE")
			time.sleep(5) # Delay to avoid multiple detections (5 seconds)

		if bh1750enabled:
			# Read from the Light Sensor
			bh1750read = bh1750.readLight()
			print("light:"+str(bh1750read))

		time.sleep(0.1) # Loop delay (1 second)


finally:
	GPIO.cleanup()
