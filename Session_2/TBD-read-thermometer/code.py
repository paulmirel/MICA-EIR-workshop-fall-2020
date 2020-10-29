import time
import board
import adafruit_thermistor

thermometer = adafruit_thermistor.Thermistor( board.TEMPERATURE, 10000, 10000, 25, 3950 )

while True:
    temp_c = thermometer.temperature
    print( temp_c )
    time.sleep( 0.2 )