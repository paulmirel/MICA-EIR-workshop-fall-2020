#import libraries
import time
import board
import analogio

#set up
angle_sensor = analogio.AnalogIn(board.A1)

#loop
while True:
    angle_normalized = round( angle_sensor.value/ 65536, 3) #the value runs from 0 to 65535, which is 2^16, 16 bits
    print( angle_normalized )

    #slow the loop only in one place
    time.sleep( 0.01 )