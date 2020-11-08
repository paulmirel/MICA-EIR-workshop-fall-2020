import time
import board
import digitalio
import busio
import adafruit_lis3dh

#initialize the accelerometer
i2c_bus_accel = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
interrupt_1 = digitalio.DigitalInOut(board.ACCELEROMETER_INTERRUPT)
accelerometer = adafruit_lis3dh.LIS3DH_I2C(i2c_bus_accel, address=0x19, int1=interrupt_1)
# Set range of accelerometer (can be RANGE_2_G, RANGE_4_G, RANGE_8_G or RANGE_16_G).
accelerometer.range = adafruit_lis3dh.RANGE_2_G

while True:
    # Read accelerometer values (in m / s ^ 2).  Returns a 3-tuple of x, y, z axis values.  Divide them by 9.806 to convert to Gs.
    a_x, a_y, a_z = [ value for value in accelerometer.acceleration ]
    print( a_z )
    time.sleep( 0.1 )