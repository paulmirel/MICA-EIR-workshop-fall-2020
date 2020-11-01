import time
import board
import analogio
import busio
from adafruit_circuitplayground import cp
import adafruit_vl53l0x

i2c_bus_offboard = busio.I2C( board.SCL, board.SDA )
rangefinder = adafruit_vl53l0x.VL53L0X( i2c_bus_offboard )


starting_color = (0,0,255)
OFF = (0,0,0)

cp.pixels.fill( starting_color )

while True:
    distance_mm = rangefinder.range
    #print( distance_mm )
    brightness = distance_mm/ 1000
    print( brightness )
    cp.pixels.brightness = brightness
    time.sleep( 0.2 )