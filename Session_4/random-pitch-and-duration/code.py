#import libraries
import time
import board
from adafruit_circuitplayground import cp
from every import Every
import random

#set up
tone_interval = Every( 5.0 ) #create the interval timer



#loop
while True:
    #in here I want to make a random range of tone duration.
    short_duration = 0.2
    long_duration = 3.3
    tone_duration = random.uniform(short_duration, long_duration)
    #print( (0, tone_duration) )

    #in here I want to make a random range of tone pitch.
    low_pitch = 300
    high_pitch = 4000
    tone_pitch = random.uniform(low_pitch, high_pitch)
    print( (tone_duration, tone_pitch) )



    cp.play_tone( tone_pitch, tone_duration ) #play a tone at 440 Hz for 2 seconds

    #slow the loop only in one place
    time.sleep( 0.1 )
