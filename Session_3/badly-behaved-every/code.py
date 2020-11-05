#import libraries
import time
import board
from adafruit_circuitplayground import cp
from every import Every

#set up
blink_interval = Every( 5.0 ) #create the blink interval timer
on_duration = Every( 2.0 )

color = ( 200, 0, 80 )
OFF = ( 0, 0, 0 )

#loop
while True:
    if blink_interval():
        cp.pixels[ 5 ] = color
    if on_duration():
        cp.pixels[ 5 ] = OFF
    #slow the loop only in one place
    time.sleep( 0.01 )

