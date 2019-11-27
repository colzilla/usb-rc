import board
import digitalio
import pulseio
from time import sleep

from adafruit_hid.gamepad import Gamepad

gp = Gamepad()

ax = pulseio.PulseIn(board.D3, 5)
ay = pulseio.PulseIn(board.A4, 5)

axmin = 1500
axmax = 1500
aymin = 1500
aymax = 1500


def range_map(x, in_min, in_max, out_min, out_max):
    x =  (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
    return x

while True:
    if len(ax) > 0 and ax[0] > 900 and ax[0] < 2100 and len(ay) > 0 and ay[0] > 900 and ay[0] < 2100: 
        try:
            xin = ax[0]
            yin = ay[0]
            if xin < axmin: axmin = xin
            if xin > axmax and xin < 2200: axmax = xin
            if yin < aymin: aymin = yin
            if yin > aymax and yin < 2200: aymax = yin
            x=range_map(xin, axmin, axmax, -127, 127)
            y=range_map(yin, aymin, aymax, -127, 127) * -1
            gp.move_joysticks(x,y)
            print("axmin", axmin, "ax", xin, "axmax", axmax, "aymin", aymin, "ay", yin, "aymax", aymax, "x", x, "y", y)
            sleep(0.02)
        except:
            print("ax", xin, "ay", yin)
            pass

    
    