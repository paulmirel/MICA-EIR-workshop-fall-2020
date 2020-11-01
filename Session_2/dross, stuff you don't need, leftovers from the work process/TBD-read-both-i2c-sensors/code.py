import time
import board
import busio
import digitalio
import adafruit_vl53l0x
import adafruit_lis3dh

i2c_bus_offboard = busio.I2C( board.SCL, board.SDA )
rangefinder = adafruit_vl53l0x.VL53L0X( i2c_bus_offboard )

#initialize the accelerometer
i2c_bus_accel = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
interrupt_1 = digitalio.DigitalInOut(board.ACCELEROMETER_INTERRUPT)
accelerometer = adafruit_lis3dh.LIS3DH_I2C(i2c_bus_accel, address=0x19, int1=interrupt_1)
# Set range of accelerometer (can be RANGE_2_G, RANGE_4_G, RANGE_8_G or RANGE_16_G).
accelerometer.range = adafruit_lis3dh.RANGE_2_G

while True:
    distance_mm = rangefinder.range
    if distance_mm > 1000:
        distance_mm = 1000
    print( distance_mm )
    a_x, a_y, a_z = [ value for value in accelerometer.acceleration ]
    print( a_z )

    time.sleep(0.1)