from adafruit_circuitplayground.express import cpx
import time

while True: 
    x, y, z = cpx.acceleration
    sum_accel = abs(x) + abs(y) + abs(z) 
    print((sum_accel, 2))
    if sum_accel < 2:
        cpx.play_file("yikes.wav")
    time.sleep(0.1)
    

        