#import libraries
import time
import board
import busio
import adafruit_vl53l0x

#set up
i2c_bus_offboard = busio.I2C( board.SCL, board.SDA )
rangefinder = adafruit_vl53l0x.VL53L0X( i2c_bus_offboard )

#loop
while True:
    distance_mm = rangefinder.range
    if distance_mm > 1000:
        distance_mm = 1000
    print( "rangefinder distance = {} mm".format( distance_mm ))

    #slow the loop only in one place
    time.sleep( 0.01 )

