#import libraries
import time
import board
from adafruit_circuitplayground import cp
from every import Every
import simpleio

#set up
#no set up required when using the cp library to read the accelerometer

#loop
while True:
    ( a_x, a_y, a_z ) = cp.acceleration
    print("z axis acceleration = {} m/s^2".format( a_z ))

    #simple division to convert to G force, 1 Earth standard gravity
    earth_gravity = 9.8
    g_z = a_z/ earth_gravity
    print("z axis acceleration = {} G".format( g_z ))

    #remapping to 16 bit integer
    g_min = -2
    g_max = 2
    out_min = 0
    out_max = 65535
    output_16_bit = int( simpleio.map_range( g_z, g_min, g_max, out_min, out_max )) #int converts from decimal to integer
    print("z axis acceleration = {} in 16 bit format".format( output_16_bit ))

    #remapping to normalized value = 0.0 to 1.0
    g_min = -2
    g_max = 2
    norm_min = 0.0
    norm_max = 1.0
    a_normalized = simpleio.map_range( g_z, g_min, g_max, norm_min, norm_max )
    print("z axis acceleration = {} normalized".format( output_16_bit ))

    #slow the loop only in one place
    time.sleep( 0.01 )