import time
import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull

#digital input pinout:
#D4 - Left Button A (must use digitalio.Pull.DOWN with this button )
#D5 - Right Button B (must use digitalio.Pull.DOWN with this button )
#D7 - Slide Switch

input_D4 = DigitalInOut(board.D4)
input_D4.direction = Direction.INPUT
input_D4.pull = digitalio.Pull.DOWN

while True:
    if input_D4.value:
        print( "button A pressed" )
    else:
        print( "button A not pressed" )
    time.sleep( 0.5 )

