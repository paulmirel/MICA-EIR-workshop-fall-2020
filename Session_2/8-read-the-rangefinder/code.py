import time
import board
import busio
import adafruit_vl53l0x

i2c_bus_offboard = busio.I2C( board.SCL, board.SDA )
rangefinder = adafruit_vl53l0x.VL53L0X( i2c_bus_offboard )

while True:
    distance_mm = rangefinder.range
    if distance_mm > 1000: #the rangefinder isn't reliable at values greater than around 1000mmm
        distance_mm = 1000 #so rather than have it jump to 8000mm, cap the value at 1000.
    print( distance_mm )
    time.sleep(0.1)