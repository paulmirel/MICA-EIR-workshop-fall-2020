import time
import board
import busio
import adafruit_vl53l0x
import neopixel
import adafruit_fancyled.adafruit_fancyled as fancy
import simpleio

#initialize the neopixels without using the cp library
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.05, auto_write=False)
pixels.fill((0, 0, 0))
pixels.show()

#initialize rangefinder
i2c_bus_offboard = busio.I2C( board.SCL, board.SDA )
rangefinder = adafruit_vl53l0x.VL53L0X( i2c_bus_offboard )

hue = 0.4

while True:
    index = 0
    while index < 10:
        #read the rangefinder distance
        distance_mm = rangefinder.range
        if distance_mm > 1000:
            distance_mm = 1000
        print( distance_mm )

        #map the rangefinder distance, 0 to 1000, into the hue range, 0.0 to 1.0
        hue = simpleio.map_range( distance_mm, 0, 1000, 0, 1)
        print( hue )

        #convert the hue into RGB
        color_hsv = fancy.CHSV( hue ) #input 0 to 1 for H, S, V :: OK to send only Hue
        color_RGB_normalized = fancy.CRGB( color_hsv )
        color_RGB = fancy.denormalize( color_RGB_normalized )

        #set the pixels, one at a time
        print( index )
        pixels[ index ] = color_RGB
        index = index + 1
        time.sleep( 0.1 )
        pixels.show() #don't forget to show() to turn the pixel on!
    #pixels.show()
    time.sleep(0.1)