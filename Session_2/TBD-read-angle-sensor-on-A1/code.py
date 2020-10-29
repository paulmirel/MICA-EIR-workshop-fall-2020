import time
import board
import analogio
angle_sensor = analogio.AnalogIn(board.A1)

while True:
    angle_normalized = round( angle_sensor.value/ 65536, 3)
    print( angle_normalized )
    time.sleep( 0.2 )
