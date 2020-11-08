import time
import board
import analogio
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.2

start_color = (120, 4, 80)
OFF = (0,0,0)

#control by position
index = 0
while index < 10:
    cp.pixels[ index ] = start_color
    cp.pixels[ index - 1 ] = OFF
    time.sleep( 0.2 )
    index = index + 1

#fill, and control brightness
brightness = 0
cp.pixels.fill( start_color )
while brightness < 1.0:
    brightness = brightness + 0.1
    cp.pixels.brightness = brightness
    time.sleep( 0.2 )

