"""
Created by: Michael Bruneau
Created on: Feb 2025
This module is a Raspberrypy Pico program that causes a light to blink and increases the durations of blinks overtime
"""

# This program uses python

import board
import digitalio
import time

# setup
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# variables
blink_delay = 1
blink_delay_increase = 1

# loop
while True:
    # turns on light and then pauses for the amount equal to the blink_delay
    led.value = True
    time.sleep(blink_delay)

     # turns off light and then pauses for the amount equal to the blink_delay
    led.value = False
    time.sleep(blink_delay)
    
    # increases blink_delay by 1 second
    blink_delay += blink_delay_increase
    
    