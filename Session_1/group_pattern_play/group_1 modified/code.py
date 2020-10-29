import time
from adafruit_circuitplayground import cp
import adafruit_fancyled.adafruit_fancyled as fancy

light_color = ( 255, 0, 150) #( red, green, blue ) each 0-255
light_color2 = (0, 100, 230)
light_color6 = (100, 100, 0)
OFF = ( 0, 0, 0 )
cp.pixels[ 1 ] = light_color
cp.pixels[ 2 ] = light_color2
cp.pixels [ 6 ] = light_color6

while True:
    x = 0
    while x < 1:
        cp.pixels.brightness = x
        print( x )
        x = x + 0.05
        time.sleep( 0.2 )
    print( "fade in complete" )
    x = 1
    while x > 0:
        cp.pixels.brightness = x
        print( x )
        x = x - 0.05
        time.sleep( 0.1 )
    print( "fade out complete" )


    index = 0
    while index < 10:
        print( index )
        cp.pixels[ index + 2 ] = light_color2
        cp.pixels[ index + 6 ] = light_color6
        index = index + 1
        time.sleep( 0.5 )