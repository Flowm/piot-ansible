#!/usr/bin/env python
# Initiates shutdown of rpi when pin 21 is set to GND

import RPi.GPIO as GPIO
import os
import time

def shutdown(channel):
    os.system("shutdown -h now 'Power button pressed'")

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(21, GPIO.FALLING, callback=shutdown, bouncetime=2000)

while 1:
    time.sleep(1)
