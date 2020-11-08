import time
import board
import analogio
import neopixel

#initialize the neopixels without using the cp library
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.05, auto_write=False)
pixels.fill((0, 0, 0))
pixels.show()

pixels.brightness = 0.2

start_color = (120, 4, 80)
OFF = (0,0,0)

#control by position
index = 0
while index < 10:
    pixels[ index ] = start_color
    pixels[ index - 1 ] = OFF
    pixels.show()
    time.sleep( 0.2 )
    index = index + 1

#fill, and control brightness
brightness = 0
pixels.fill( start_color )
while brightness < 1.0:
    brightness = brightness + 0.1
    pixels.brightness = brightness
    pixels.show()
    time.sleep( 0.2 )

