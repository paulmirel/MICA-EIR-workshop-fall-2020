import time
import board
import analogio

light_sensor = analogio.AnalogIn(board.LIGHT)

while True:
    light_level = light_sensor.value
    print( light_level )
    time.sleep( 0.2 )