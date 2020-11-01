import time
import board
import analogio
from adafruit_circuitplayground import cp

angle_sensor = analogio.AnalogIn(board.A1)

while True:
    angle_normalized = round( angle_sensor.value/ 65536, 3)
    print( angle_normalized )
    if angle_normalized > 0.5:
        cp.pixels[0] = (0,0,255)
    else:
        cp.pixels[0] = (0,0,0)
    time.sleep( 0.2 )