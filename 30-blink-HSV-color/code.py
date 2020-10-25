import time
from adafruit_circuitplayground import cp
import adafruit_fancyled.adafruit_fancyled as fancy

hue = 0.008
sat = 1.0
val = 1.0

color_hsv = fancy.CHSV( hue, sat, val ) #input 0 to 1 for H, S, V :: OK to send only Hue
print( "Hue normalized = {}".format( color_hsv.hue ))
#print( "Saturation normalized = {}".format( color_hsv.saturation ))
#print( "Value normalized = {}".format( color_hsv.value ))
color_RGB_normalized = fancy.CRGB( color_hsv )
print( "Color RGB normalized = {}".format( color_RGB_normalized ))
color_RGB = fancy.denormalize( color_RGB_normalized )
print ( "Color RGB 0-255 = {}".format( color_RGB ))

cp.pixels.brightness = 0.2 # 0.0 to 1.0 Overall brightness modifier

light_color = color_RGB #( red, green, blue ) each 0-255
OFF = ( 0, 0, 0 )

while True:
    cp.pixels[ 1 ] = light_color
    time.sleep( 0.5 )
    cp.pixels[ 1 ] = OFF
    time.sleep( 0.5 )