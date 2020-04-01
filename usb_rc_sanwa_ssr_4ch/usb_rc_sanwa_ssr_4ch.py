import board
import digitalio
import pulseio
from adafruit_hid.gamepad import Gamepad
from time import sleep
import sys

version="20200331-1933"
print("usb-rc version [{}] - an adapter from RC car receiver to USB-gamepad/joystick. https://github.com/colzilla/usb-rc".format(version))

debug=False

gamepad = Gamepad()

#setup the pulse readers
ch1 = pulseio.PulseIn(board.A1, 1)
ch2 = pulseio.PulseIn(board.A2, 1)
ch3 = pulseio.PulseIn(board.A3, 1)
ch4 = pulseio.PulseIn(board.A4, 1)

#used in auto-calibration
ch1min = ch2min = ch3min = ch4min = 279
ch1max = ch2max = ch3max = ch4max = 281

allowed_min = 100
allowed_max = 480


def range_map(x, in_min, in_max, out_min, out_max):
    joy_value =  (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
    return joy_value

while True:

    if len(ch1) > 0: ch1in = ch1[0] 
    else: ch1in = 280
    if len(ch2) > 0: ch2in = ch2[0] 
    else: ch2in = 280
    if len(ch3) > 0: ch3in = ch3[0] 
    else: ch3in = 280
    if len(ch4) > 0: ch4in = ch4[0] 
    else: ch4in = 280

    try:
        if ch1in < ch1min and ch1in > allowed_min: ch1min = ch1in
        if ch1in > ch1max and ch1in < allowed_max: ch1max = ch1in
        if ch2in < ch2min and ch2in > allowed_min: ch2min = ch2in
        if ch2in > ch2max and ch2in < allowed_max: ch2max = ch2in
        if ch3in < ch3min and ch3in > allowed_min: ch3min = ch3in
        if ch3in > ch3max and ch3in < allowed_max: ch3max = ch3in
        if ch4in < ch4min and ch4in > allowed_min: ch4min = ch4in
        if ch4in > ch4max and ch4in < 480: ch4max = ch4in

        x=range_map(ch1in, ch1min, ch1max, -127, 127)
        y=range_map(ch2in, ch2min, ch2max, -127, 127) * -1
        z=range_map(ch3in, ch3min, ch3max, -127, 127) * -1
        r=range_map(ch4in, ch4min, ch4max, -127, 127) * -1

        gamepad.move_joysticks(x, y, z, r)
        if(debug): print("ch1 {:04d}/{:04d}/{:04d} ".format(ch1min, ch1in, ch1max), end = " ")
        if(debug): print("ch2 {:04d}/{:04d}/{:04d} ".format(ch2min, ch2in, ch2max), end = " ")
        if(debug): print("ch3 {:04d}/{:04d}/{:04d} ".format(ch3min, ch3in, ch3max), end = " ")
        if(debug): print("ch4 {:04d}/{:04d}/{:04d} ".format(ch4min, ch4in, ch4max), end = " ")
        if(debug): print("x[{:>4}] y[{:>4}] z[{:>4}] r[{:>4}] ".format(x, y, z, r))

#        sleep(0.001)
    except Exception as e:
        pass


    
    

