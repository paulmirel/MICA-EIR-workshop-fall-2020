#import libraries
import time
import board
import touchio
from board import *

#set up
touch_A4 = touchio.TouchIn(A4)

#loop
while True:
    if touch_A4.value:
        print( "A4 touched" )
    else:
        print( "A4 open" )

    #slow the loop only in one place
    time.sleep( 0.01 )