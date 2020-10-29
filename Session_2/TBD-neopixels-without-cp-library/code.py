import time
import board
import neopixel
import adafruit_fancyled.adafruit_fancyled as fancy

#initialize the neopixels without using the cp library
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.05, auto_write=False)
pixels.fill((0, 0, 0))
pixels.show()

hue = 0.4

color_hsv = fancy.CHSV( hue ) #input 0 to 1 for H, S, V :: OK to send only Hue
color_RGB_normalized = fancy.CRGB( color_hsv )
color_RGB = fancy.denormalize( color_RGB_normalized )

while True:
    index = 0
    while index < 10:
        print( index )
        pixels[ index ] = color_RGB
        index = index + 1
        time.sleep( 0.5 )
        #pixels.show()
    #pixels.show()
    time.sleep(0.1)