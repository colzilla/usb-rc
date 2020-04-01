import board
import digitalio
import pulseio
from adafruit_hid.gamepad import Gamepad
from time import sleep
import sys
import adafruit_dotstar as dotstar

onboard_led = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=1)

red = 0xff0000
green = 0x00ff00
blue = 0x0000ff

onboard_led[0] = red
sleep(0.5)
onboard_led[0] = green
sleep(0.5)
onboard_led[0] = blue
sleep(0.5)

startpause = 1
print("usb-rc - an adapter from RC car receiver to USB-gamepad/joystick. https://github.com/colzilla/usb-rc")
print("starting in {} sec...".format(startpause))
sleep(startpause)

debug=True
verbose=True

#create the gampepad object
gp = Gamepad()

#setup the pulse readers
ch1 = pulseio.PulseIn(board.A1, 1)
ch2 = pulseio.PulseIn(board.A2, 1)
ch3 = pulseio.PulseIn(board.A3, 1)
ch4 = pulseio.PulseIn(board.A4, 1)

#used in auto-calibration
ch1min = ch2min = ch3min = ch4min = 279
ch1max = ch2max = ch3max = ch4max = 281

allowed_min = 130
allowed_max = 480

loop = 0

def range_map(x, in_min, in_max, out_min, out_max):
    joy_value =  (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
    return joy_value

while True:
    loop += 1

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

        gp.move_joysticks(x, y, z, r)
        if(debug): print("ch1 min[{}] now[{}] max[{}] ch2 min[{}] now[{}] max[{}] ch3 min[{}] now[{}] max[{}] ch4 min[{}] now[{}] max[{}]")

#, ch1min, "ch1in", ch1in, "ch1max", ch1max, "|| ",
#                         "ch2min", ch2min, "ch2in", ch2in, "ch2max", ch2max, "|| ",
#                         "ch3min", ch3min, "ch3in", ch3in, "ch3max", ch3max, "|| ",
#                         "ch4min", ch4min, "ch4in", ch4in, "ch4max", ch4max, 
#                         "joy_x", x, "joy_y", y, "joy_z", z, "joy_r", r)

        sleep(0.005)
    except Exception as e:
        pass


    
    

