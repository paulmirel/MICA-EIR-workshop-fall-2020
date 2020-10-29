import time
import board
import analogio
import digitalio
import busio
import adafruit_vl53l0x
import adafruit_lis3dh
import adafruit_thermistor


#initialize the thermometer
thermometer = adafruit_thermistor.Thermistor( board.TEMPERATURE, 10000, 10000, 25, 3950 )

#initialize the light sensor
light_sensor = analogio.AnalogIn(board.LIGHT)

#initialize the angle sensor
angle_sensor = analogio.AnalogIn(board.A1)

#initialize the rangefinder
i2c_bus_offboard = busio.I2C( board.SCL, board.SDA )
rangefinder = adafruit_vl53l0x.VL53L0X( i2c_bus_offboard )

#initialize the accelerometer
i2c_bus_accel = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
interrupt_1 = digitalio.DigitalInOut(board.ACCELEROMETER_INTERRUPT)
accelerometer = adafruit_lis3dh.LIS3DH_I2C(i2c_bus_accel, address=0x19, int1=interrupt_1)
# Set range of accelerometer (can be RANGE_2_G, RANGE_4_G, RANGE_8_G or RANGE_16_G).
accelerometer.range = adafruit_lis3dh.RANGE_2_G

while True:
    if True:
        angle_normalized = round( angle_sensor.value/ 65536, 3)
        print( "Angle = {}".format( angle_normalized ))
    if True:
        temp_c = thermometer.temperature
        print( "Temperature = {} C".format( temp_c ))
    if True:
        light_level = light_sensor.value
        print( "Light level = {}".format( light_level ))
    if True:
        distance_mm = rangefinder.range
        if distance_mm > 1000:
            distance_mm = 1000
        print( "rangefinder distance = {} mm".format( distance_mm ))
    if True:
        a_x, a_y, a_z = [ value for value in accelerometer.acceleration ]
        print( "acceleration in Z direction = {} m/s^2".format( a_z ))
    time.sleep(0.1)