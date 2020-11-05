#import libraries
import time
import board
import adafruit_thermistor

#set up
thermometer = adafruit_thermistor.Thermistor( board.TEMPERATURE, 10000, 10000, 25, 3950 )
# 1. board.Temperature is the Analog input that the termistor is connected to.
# 2. the first 10000 is the fixed readout resistor's resistance in Ohms. Also known as the Series Resistor.
# 3. the second 10000 is the Nominal resistance (Ro), the value of the thermistor's resistance at a nominal temperature.
# 4. 25 is the Nominal temperature (To), at its nominal resistance value.
# 5. 3950 is the temperature coefficient of resistance for the thermistor, known as the Beta coefficient
# 6. You can add a sixth parameter, a High_side boolean, to indicate if the thermistor is connected on the high side or low side of the resistor voltage divider.
# the default value for the High_side boolean is true, meaning that the thermistor is connected from power to analog_in, and the series resistor is connected from analog_in to ground.
# since you are setting these values for a specific thermistor, if you set them incorrectly your temperature reading will be incorrect.


#loop
while True:
    temp_c = thermometer.temperature
    print( "Temperature = {} C".format( temp_c )) #easy to read

    #slow the loop only in one place
    time.sleep( 0.01 )