from adafruit_circuitplayground import cp
from unrvl.every import Every

cp.pixels.brightness = 0.6 # 0.0 to 1.0
light_color = ( 255, 0, 0 ) #( red, green, blue ) each 0-255
OFF = ( 0, 0, 0 )

pixel_one_delay = Every(0.5) # every 1/2 second, ...
pixel_two_delay = Every(1/3) # every 1/3 second, ...

while True:
    # Blink pixel 1
    if pixel_one_delay():
        if cp.pixels[ 1 ] == OFF:
            cp.pixels[ 1 ] = light_color
        else:
            cp.pixels[ 1 ] = OFF

    # Blink pixel 2
    if pixel_two_delay():
        if cp.pixels[ 2 ] == OFF:
            cp.pixels[ 2 ] = light_color
        else:
            cp.pixels[ 2 ] = OFF

