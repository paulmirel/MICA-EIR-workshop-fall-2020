import time
from adafruit_circuitplayground import cp
cp.pixels.brightness = 0.2

OFF = ( 0, 0, 0 )

while True:
    x = 0
    while x < 255:
        light_color = ( x, 0, 0 ) #( red, green, blue ) each 0-255
        cp.pixels.fill ( light_color )
        print( x )
        x = x + 1
        time.sleep( 0.01 )
