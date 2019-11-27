import board
import digitalio
import pulseio
from adafruit_hid.gamepad import Gamepad
from time import sleep
import sys

debug=False

#create the gampepad object
gp = Gamepad()

#setup the pulse readers
ch1 = pulseio.PulseIn(board.A3, 5)
ch2 = pulseio.PulseIn(board.A4, 5)

#used in auto-calibration
ch1min = 1499
ch1max = 1501
ch2min = 1499
ch2max = 1501
allowed_min = 800
allowed_max = 2200
loop=0

def range_map(x, in_min, in_max, out_min, out_max):
    joy_value =  (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
    return joy_value

while True:
    if(debug): print("\nloop[{}]".format(loop))
    loop += 1

    if len(ch1) > 0: 
        ch1in = ch1[0] 
        if(debug): print("ch1 was ", ch1in)
    else: 
        if(debug): print("ch1 was empty")
        ch1in = 1500
    
    if len(ch2) > 0: 
        ch2in = ch2[0] 
        if(debug): print("ch2 was ", ch2in)
    else: 
        if(debug): print("ch2 was empty")
        ch2in = 1500

#    and xin > allowed_min and xin < allowed_max and yin > allowed_min and yin < allowed_max: 
    try:
        if ch1in < ch1min: ch1min = ch1in
        if ch1in > ch1max and ch1in < 2200: ch1max = ch1in
        if ch2in < ch2min: ch2min = ch2in
        if ch2in > ch2max and ch2in < 2200: ch2max = ch2in
        x=range_map(ch1in, ch1min, ch1max, -127, 127)
        y=range_map(ch2in, ch2min, ch2max, -127, 127) * -1
        gp.move_joysticks(x,y)
        if(debug): print("ch1min", ch1min, "ch1in", ch1in, "ch1max", ch1max, "ch2min", ch2min, "ch2in", ch2in, "ch2max", ch2max, "joy_x", x, "joy_y", y)
        print("x", x, ", y", y)
        sleep(0.001)
    except Exception as e:
        if(debug): print("ax", ch1in, "ay", ch2in, e)
        pass

    # if(debug): sleep(0.5)

    
    
