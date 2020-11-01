import time
import board
import analogio
angle_sensor = analogio.AnalogIn(board.A1)

while True:
    angle_normalized = round( angle_sensor.value/ 65536, 3) #the value runs from 0 to 65535, which is 2^16, 16 bits
    print( angle_normalized )
    time.sleep( 0.2 )