#import libraries
import time
import board
from adafruit_circuitplayground import cp
from every import Every

#set up
warning_interval = Every( 0.8 ) #create the interval timer
warning_color = ( 255, 0, 0 )
OFF = ( 0, 0, 0 )

#loop
while True:
    ( a_x, a_y, a_z ) = cp.acceleration
    print((0, a_z))
    cp.pixels.fill( OFF )
    if a_z < -0.5:
        if warning_interval(): #remember the () to check the time. an object without () is always True, because it exists.
            cp.play_tone( 880, 0.5 ) #play a tone
            cp.pixels.fill( warning_color )
            time.sleep( 0.05 )
        else:
            cp.pixels.fill( OFF )
    #slow the loop only in one place
    time.sleep( 0.01 )