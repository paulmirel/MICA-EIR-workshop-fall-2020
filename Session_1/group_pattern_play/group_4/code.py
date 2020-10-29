import time
from adafruit_circuitplayground import cp
import adafruit_fancyled.adafruit_fancyled as fancy

cp.pixels.brightness = 0.3 # 0.0 to 1.0 Overall brightness modifier

hue = 0.9
sat = 1.0
val = 1.0
OFF = ( 0, 0, 0 )

color_RGB = fancy.denormalize( fancy.CRGB( fancy.CHSV( hue, sat, val ))) #collapse three steps

while True:
    index = 0
    while index < 10:
        print( index )
        cp.pixels[ index - 1 ] = 210
        cp.pixels[ index ] = 10
        cp.pixels[ index ] = 255
        cp.pixels[ index ] = color_RGB
        index = index + 3
        time.sleep( 0.2 )