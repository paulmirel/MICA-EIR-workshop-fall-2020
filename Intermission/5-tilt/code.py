# heartbeat, tilt, fade, tap

import time
from adafruit_circuitplayground import cp
from unrvl.every import Every

cp.pixels.brightness = 0.6 # 0.0 to 1.0
light_color = ( 255, 0, 0 ) #( red, green, blue ) each 0-255
OFF = ( 0, 0, 0 )

heartbeat = Every(2.5) # I like heartbeats

tilt_update = Every(0.08) # cf. interaction responsiveness guidelines
# which pixels for tilt:
left_tilt = (1,2,3)
right_tilt = (6,7,8)

# tilt color and fade
tilt_color = (0,1,5)
tap_brightness = 100 # increase blue to this on tap
fade_amount = 10
fade_rate = Every( 1.0 / ( (tap_brightness - tilt_color[2]) / fade_amount) ) # fade in 1 second
print("fades every",fade_rate.interval)
tilt_fade_color = list(tilt_color) # lists are changeable, tuples aren't

cp.taps = 1 # detect single taps

max_loop_time = 0 # we are going to measure

# This loop takes 0.05 seconds to run! python is slow
while True:
    loop = time.monotonic()

    if heartbeat():
        cp.red_led = not cp.red_led # clever blink: true/false

    # update the tilt every 100msec
    if tilt_update():
        # actually, "pixels" is sloooow, so only do so often:

        # 0 when level, positive when a5 is lower, negative when a1 is lower
        x = cp.acceleration.x
        if x > 1.0: # very sensitive
            for i in left_tilt:
                cp.pixels[ i ] = tilt_fade_color
            for i in right_tilt:
                cp.pixels[ i ] = OFF
        elif x < -1.0:
            for i in right_tilt:
                cp.pixels[ i ] = tilt_fade_color
            for i in left_tilt:
                cp.pixels[ i ] = OFF

    # tap means, start bright, then fade out
    if cp.tapped:
        tilt_fade_color = list(tilt_color)
        tilt_fade_color[2] = tap_brightness # more blue!

    if fade_rate():
        # just fade the blue part
        if tilt_fade_color[2] > tilt_color[2]:
            # don't go below our base brightness...
            tilt_fade_color[2] = max( tilt_color[2], tilt_fade_color[2] - fade_amount)

    loop_time = time.monotonic() - loop
    if loop_time > max_loop_time:
        print(loop_time)
        max_loop_time = loop_time

