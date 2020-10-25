import time
from adafruit_circuitplayground import cp

light_color = ( 255, 0, 0 ) #( red, green, blue ) each 0-255
OFF = ( 0, 0, 0 )
cp.pixels[ 1 ] = light_color

x = 0
while x < 1:
    cp.pixels.brightness = x
    print( x )
    x = x + 0.05
    time.sleep( 0.1 )

x = 1
while x > 0:
    cp.pixels.brightness = x
    print( x )
    x = x - 0.05
    time.sleep( 0.1 )