import time
import board
from digitalio import DigitalInOut, Direction, Pull

output_A6 = DigitalInOut(board.A6)
output_A6.direction = Direction.OUTPUT

while True:
    output_A6.value = True
    time.sleep( 0.5 )
    output_A6.value = False
    time.sleep( 0.5 )

