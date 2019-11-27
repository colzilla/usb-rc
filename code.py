import board
import digitalio
import pulseio
from adafruit_hid.gamepad import Gamepad
from time import sleep

#create the gampepad object
gp = Gamepad()

#setup the pulse readers
ch1 = pulseio.PulseIn(board.A3, 1)
ch2 = pulseio.PulseIn(board.A4, 1)

#used in auto-calibration
ch1min = 1500
ch1max = 1500
ch2min = 1500
ch2max = 1500
allowed_min = 900
allowed_max = 2200

def range_map(x, in_min, in_max, out_min, out_max):
    joy_value =  (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
    return joy_value

while True:
    if len(ch1) > 0: 
        xin = ch1[0] 
    else 
        xin = 1500
    
    if len(ch2) > 0: 
        yin = ch2[0] 
    else 
        yin = 1500
        
    and xin > allowed_min and xin < allowed_max and yin > allowed_min and yin < allowed_max: 
        try:
            if xin < axmin: axmin = xin
            if xin > axmax and xin < 2200: axmax = xin
            if yin < aymin: aymin = yin
            if yin > aymax and yin < 2200: aymax = yin
            x=range_map(xin, axmin, axmax, -127, 127)
            y=range_map(yin, aymin, aymax, -127, 127) * -1
            gp.move_joysticks(x,y)
            print("axmin", axmin, "ax", xin, "axmax", axmax, "aymin", aymin, "ay", yin, "aymax", aymax, "x", x, "y", y)
            sleep(0.01)
        except:
            print("ax", xin, "ay", yin)
            pass

    
    
