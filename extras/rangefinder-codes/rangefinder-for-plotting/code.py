import time
import board
import busio
import adafruit_vl53l0x

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_vl53l0x.VL53L0X(i2c)

while True:
    #print('Range: {}mm'.format(sensor.range))
    distance_mm = sensor.range
    if distance_mm > 1000:
        distance_mm = 1000
    distance_tuple = ( 0, distance_mm )
    print( distance_tuple )
    time.sleep(0.1)