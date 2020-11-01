import time
import board
import busio
import adafruit_vl53l0x
import simpleio
import neopixel #not enough memory available to load the whole cp library, so we only load the neopixel part of it
import adafruit_fancyled.adafruit_fancyled as fancy

#initialize the neopixels without using the cp library
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.05, auto_write=False)
pixels.fill((0, 0, 0))
pixels.show()

i2c_bus_offboard = busio.I2C( board.SCL, board.SDA )
rangefinder = adafruit_vl53l0x.VL53L0X( i2c_bus_offboard )

color_RGB = (0,0,255)

while True:
    distance_mm = rangefinder.range
    if distance_mm > 1000: #the rangefinder isn't reliable at values greater than around 1000mmm
        distance_mm = 1000 #so rather than have it jump to 8000mm, cap the value at 1000.
    print( distance_mm )

    #set up the ranges for remapping
    distance_mm_minimum = 100
    distance_mm_maximum = 600

    hue_minimum = 0.0
    hue_maximum = 1.0

    hue = simpleio.map_range(distance_mm, distance_mm_minimum, distance_mm_maximum, hue_minimum, hue_maximum)

    #convert hue to RGB
    color_hsv = fancy.CHSV( hue ) #input 0 to 1 for H, S, V :: OK to send only Hue
    color_RGB_normalized = fancy.CRGB( color_hsv )
    color_RGB = fancy.denormalize( color_RGB_normalized )

    pixels.fill( color_RGB )
    pixels.show() #must remember to do pixels.show() when using the neopixel library.
                    #pixels.show() is not needed when using the cp library.
    time.sleep(0.01)