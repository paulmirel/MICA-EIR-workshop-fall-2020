#import libraries
import time
import board
from adafruit_circuitplayground import cp

#set up
#no set up required when using the cp library

#loop
while True:
    temp_c = cp.temperature
    print( "Temperature = {} C".format( temp_c )) #easy to read

    #slow the loop only in one place
    time.sleep( 0.01 )