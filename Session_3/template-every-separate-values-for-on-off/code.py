#import libraries
import time
import board
from adafruit_circuitplayground import cp
from every import Every

#set up
blink_interval = Every( 1.0 ) #create the blink interval timer
on_duration = 0.5
off_duration = 2.0

color = ( 200, 0, 80 )
OFF = ( 0, 0, 0 )

#loop
while True:
    if blink_interval():
       if cp.pixels[5] == OFF: # if already off, then
           cp.pixels[ 5 ] = color
           blink_interval.interval = on_duration # change to the on duration for the next check.
       else: # if already on, then
           cp.pixels[ 5 ] = OFF
           blink_interval.interval = off_duration # change to the off duration for the next check.
    #slow the loop only in one place
    time.sleep( 0.01 )