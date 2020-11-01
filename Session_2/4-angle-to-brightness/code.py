import time
import board
import analogio
from adafruit_circuitplayground import cp

angle_sensor = analogio.AnalogIn(board.A1)

starting_color = (0,0,255)
OFF = (0,0,0)

cp.pixels.fill( starting_color )

while True:
    angle_normalized = round( angle_sensor.value/ 65536, 3)
    print( angle_normalized )
    cp.pixels.brightness = angle_normalized
    time.sleep( 0.2 )