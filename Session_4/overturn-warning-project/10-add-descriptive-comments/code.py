# overturn warning. sounds an alarm and flashes lights when circuit playground is oriented component side down.
# Paul Pirel 20201007 for MICA Engineer in Residence Workshop: Electronics for Artworks

#import libraries
import time
import board
from adafruit_circuitplayground import cp
from every import Every #Every non-blocking timer written by Alan Grover

#set up
warning_interval = Every( 0.8 ) #create the interval timer
warning_color = ( 255, 0, 0 )
flash_duration = Every(0.1, 0) # note the trailing 0
tone_duration = Every(0.5, 0) # note the trailing 0
OFF = ( 0, 0, 0 )

#loop
while True:
    ( a_x, a_y, a_z ) = cp.acceleration
    #print((0, a_z))

    if a_z < -0.5:
        if warning_interval(): #remember the () to check the time. an object without () is always True, because it exists.
            cp.start_tone( 880 ) # start a tone, non-blocking!
            cp.pixels.fill( warning_color )

            # you have to "start" timers
            flash_duration.start()
            tone_duration.start()

    # when to stop the tone
    if tone_duration():
        cp.stop_tone()

    # when to turn off
    if flash_duration():
        cp.pixels.fill( OFF )

    #slow the loop only in one place
    time.sleep( 0.01 )
