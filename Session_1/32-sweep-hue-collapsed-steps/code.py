import time
from adafruit_circuitplayground import cp
import adafruit_fancyled.adafruit_fancyled as fancy

cp.pixels.brightness = 0.2 # 0.0 to 1.0 Overall brightness modifier

hue = 0.0
sat = 1.0
val = 1.0

while True:
    hue = 0.0
    while hue < 1:
        #color_hsv = fancy.CHSV( hue, sat, val ) #input 0 to 1 for H, S, V :: OK to send only Hue
        #color_RGB_normalized = fancy.CRGB( color_hsv )
        #color_RGB = fancy.denormalize( color_RGB_normalized )
        color_RGB = fancy.denormalize( fancy.CRGB( fancy.CHSV( hue, sat, val ))) #collapse three steps
        print ( "Color RGB 0-255 = {}".format( color_RGB ))
        cp.pixels.fill( color_RGB )
        hue = hue + 0.01
        time.sleep( 0.01 )