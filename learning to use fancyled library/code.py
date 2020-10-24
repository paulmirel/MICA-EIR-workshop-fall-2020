import time
from adafruit_circuitplayground import cp
import adafruit_fancyled.adafruit_fancyled as fancy
#import denormalize from adafruit_fancyled

hue = 0.006

sat = 1.0
val = 1.0


color_hsv = fancy.CHSV( hue, sat, val ) #input 0 to 1 for H, S, V :: OK to send only Hue
print( color_hsv.hue )
print( color_hsv.saturation )
print( color_hsv.value )
color_RGBd = fancy.CRGB( color_hsv )
print( color_RGBd )
color_RGB = fancy.denormalize( color_RGBd )
print ( color_RGB )



cp.pixels.brightness = 0.2 # 0.0 to 1.0
light_color = color_RGB #( red, green, blue ) each 0-255
OFF = ( 0, 0, 0 )

while True:
    cp.pixels[ 1 ] = light_color
    time.sleep( 0.5 )
    cp.pixels[ 1 ] = OFF
    time.sleep( 0.5 )