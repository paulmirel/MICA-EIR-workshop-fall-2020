#import libraries
import time
import board
import analogio

#set up
light_sensor = analogio.AnalogIn( board.LIGHT )

#loop
while True:
    light_level = light_sensor.value
    print( "Light level = {}".format( light_level ))

    #slow the loop only in one place
    time.sleep( 0.01 )