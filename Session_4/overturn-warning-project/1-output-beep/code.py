#import libraries
import time
import board
from adafruit_circuitplayground import cp
from every import Every

#set up
tone_interval = Every( 0.8 ) #create the interval timer

#loop
while True:
    if tone_interval(): #remember the () to check the time. tone_interval without () is always True, because it exists.
        cp.play_tone( 880, 0.5 ) #play a tone at 440 Hz for 2 seconds

    #slow the loop only in one place
    time.sleep( 0.01 )