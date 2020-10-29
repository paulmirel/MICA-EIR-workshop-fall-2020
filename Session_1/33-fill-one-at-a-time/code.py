import time
from adafruit_circuitplayground import cp
import adafruit_fancyled.adafruit_fancyled as fancy

cp.pixels.brightness = 0.2 # 0.0 to 1.0 Overall brightness modifier

hue = 0.1
sat = 1.0
val = 1.0

color_RGB = fancy.denormalize( fancy.CRGB( fancy.CHSV( hue, sat, val ))) #collapse three steps

while True:
    index = 0
    while index < 10:
        print( index )
        cp.pixels[ index ] = color_RGB
        index = index + 1
        time.sleep( 0.5 )