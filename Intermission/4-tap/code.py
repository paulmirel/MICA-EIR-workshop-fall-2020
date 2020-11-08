# tap, timed leds

from adafruit_circuitplayground import cp
from unrvl.every import Every

cp.pixels.brightness = 0.6 # 0.0 to 1.0
light_color = ( 0, 10, 30 ) #( red, green, blue ) each 0-255
OFF = ( 0, 0, 0 )

heartbeat = Every(1.5) # I like heartbeats

long_led = 2
short_led = 7

# timers ("once"), have a trailing 0
long_on = Every(2,0) # a 2 second timer
short_on = Every(0.5,0) # a shorter timer

cp.taps = 1 # detect single taps

while True:

    if heartbeat():
        cp.red_led = not cp.red_led # clever blink: true/false

    # tap! turn on leds
    if cp.tapped:
        cp.pixels[ long_led ] = light_color
        cp.pixels[ short_led ] = light_color

        # timers don't run till you .start() them
        long_on.start()
        short_on.start()

    if long_on(): # "expired?"
        cp.pixels[ long_led ] = OFF

    if short_on(): # "expired?"
        cp.pixels[ short_led ] = OFF

