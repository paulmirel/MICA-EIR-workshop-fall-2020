import time
import board
import analogio
import neopixel
import adafruit_fancyled.adafruit_fancyled as fancy

#initialize the neopixels without using the cp library
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.05, auto_write=False)
pixels.fill((0, 0, 0))
pixels.show()

pixels.brightness = 0.2

start_color = (120, 4, 80)
OFF = (0,0,0)

#control by hue
sat = 1.0 #must put 1.0 to force fancy to use normalized values. If 1, fancy thinks it is 0-255.
val = 1.0 #must put 1.0 to force fancy to use normalized values. If 1, fancy thinks it is 0-255.
hue = 0

while hue < 1.0:
    #convert hue, sat, val to RGB
    color_hsv = fancy.CHSV( hue , sat, val ) #input 0 to 1 for H, S, V :: OK to send only Hue
    color_RGB_normalized = fancy.CRGB( color_hsv )
    color_RGB = fancy.denormalize( color_RGB_normalized )
    print( color_RGB )

    pixels.fill( color_RGB )
    pixels.show()
    hue = hue + 0.1
    time.sleep( 0.2 )

hue = 0.3
sat = 1.0
val = 1.0

while sat > 0:
    #convert hue, sat, val to RGB
    color_hsv = fancy.CHSV( hue , sat, val ) #input 0 to 1 for H, S, V :: OK to send only Hue
    color_RGB_normalized = fancy.CRGB( color_hsv )
    color_RGB = fancy.denormalize( color_RGB_normalized )
    print( color_RGB )

    pixels.fill( color_RGB )
    pixels.show()
    sat = sat - 0.01
    time.sleep( 0.02 )

hue = 0.8
sat = 1.0
val = 0

while val < 1:
    #convert hue, sat, val to RGB
    color_hsv = fancy.CHSV( hue , sat, val ) #input 0 to 1 for H, S, V :: OK to send only Hue
    color_RGB_normalized = fancy.CRGB( color_hsv )
    color_RGB = fancy.denormalize( color_RGB_normalized )
    print( color_RGB )

    pixels.fill( color_RGB )
    pixels.show()
    val = val + 0.01
    time.sleep( 0.02 )


