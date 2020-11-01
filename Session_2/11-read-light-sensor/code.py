import time
import board
import analogio

light_sensor = analogio.AnalogIn( board.LIGHT )

while True:
    light_level = light_sensor.value
    #print( "Light level = {}".format( light_level )) #easy to read
    print ((light_level, 0)) #easy to plot, click the Plotter button on the Mu editor
    time.sleep( 0.2 )