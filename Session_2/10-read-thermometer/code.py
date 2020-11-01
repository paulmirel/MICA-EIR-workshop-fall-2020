import time
import board
from adafruit_circuitplayground import cp

while True:
    temp_c = cp.temperature
    #print( "Temperature = {} C".format( temp_c )) #easy to read
    print ((temp_c, 20)) #easy to plot, click the Plotter button on the Mu editor
    time.sleep( 0.2 )