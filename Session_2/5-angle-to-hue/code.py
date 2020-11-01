import time
import board
import analogio
from adafruit_circuitplayground import cp
import adafruit_fancyled.adafruit_fancyled as fancy

angle_sensor = analogio.AnalogIn(board.A1)

starting_color = (0,0,255)
OFF = (0,0,0)

cp.pixels.fill( starting_color )

while True:
    angle_normalized = round( angle_sensor.value/ 65536, 3)
    print( angle_normalized )
    hue = angle_normalized
    color_hsv = fancy.CHSV( hue ) #input 0 to 1 for H, S, V :: OK to send only Hue
    color_RGB_normalized = fancy.CRGB( color_hsv )
    color_RGB = fancy.denormalize( color_RGB_normalized )
    cp.pixels.fill( color_RGB )
    time.sleep( 0.2)