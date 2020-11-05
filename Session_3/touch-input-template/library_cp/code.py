#import libraries
import time
import board
from adafruit_circuitplayground import cp

#set up
#none needed for touch input when using the cp library

#loop
while True:
    if cp.touch_A4:
        print( "A4 touched" )
    else:
        print( "A4 open" )

    #slow the loop only in one place
    time.sleep( 0.01 )