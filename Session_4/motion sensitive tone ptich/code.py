#import libraries
import time
import board
from adafruit_circuitplayground import cp
import random
import simpleio

#loop
while True:
    #in here I want to read the accelerometer and get a number that tells me how how much total acceleration there is right now.
    x, y, z = cp.acceleration
    sum_accel = abs(x) + abs(y) + abs(z)
    #print((sum_accel, 2))
    #the range of sum_accel is about 0 to 150
    accel_min = 0
    accel_max = 150

    #in here I want to make a random range of tone duration.
    short_duration = 0.1
    long_duration = 0.6
    tone_duration = random.uniform(short_duration, long_duration)
    #print( (0, tone_duration) )

    #in here I want to make a random range of tone pitch.
    low_pitch = 300
    high_pitch = 1000
    #tone_pitch = random.uniform(low_pitch, high_pitch)
    #print( (tone_duration, tone_pitch) )

    tone_pitch = simpleio.map_range( sum_accel, accel_min, accel_max, low_pitch, high_pitch )
    print( (300, tone_pitch) )

    cp.play_tone( tone_pitch, tone_duration ) #play a tone at 440 Hz for 2 seconds

    #slow the loop only in one place
    time.sleep( 0.1 )