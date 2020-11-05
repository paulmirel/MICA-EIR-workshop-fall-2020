#import libraries
import time
import board
from adafruit_circuitplayground import cp
from every import Every

#set up
blink_interval = Every( 1.0 ) #create the blink interval timer

color = ( 200, 0, 80 )
OFF = ( 0, 0, 0 )

#loop
while True:
    if blink_interval():
       if cp.pixels[5] == OFF: # if already off, then
           cp.pixels[ 5 ] = color
       else: # if already on, then
           cp.pixels[ 5 ] = OFF
    #slow the loop only in one place
    time.sleep( 0.01 )
