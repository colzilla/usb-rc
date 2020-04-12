# usb-rc
AdaFruit ~~Trinket M0 and~~ ItsyBitsy M4 USB adapter for RC receivers.

The Trinkets have a much slower CPU than the ItsyBitsy M4, and although that's not been an issue on the one I made, Ive had reports of some jittering on some combinations of RX and PC, so I'm no longer recommending them.  YMMV.

***update - please take the time to watch the video kindly created by Matt Spencer from Vancouver, British Columbia!***
https://www.youtube.com/watch?v=9zhCrwn6ba0

Install

1. Copy the "adafruit_hid" folder and the "code.py" file to the CIRCUITPY folder on your AdaFruit ItsyBitsy
2. Connect the RX GND to the "G" pin on the Itsy
3. Connect the RX 5V to the "USB" pin on the Itsy
4. Connect the RX CH1 to the "A3" pin on the Itsy
5. Connect the RX CH2 to the "A4" pin on the Itsy

See the images folder for pictures.
![itsy](https://github.com/colzilla/usb-rc/blob/master/images/IMG_9010.jpg)
![sanwa_rx](https://github.com/colzilla/usb-rc/blob/master/images/IMG_9023.jpg)

Connect the itsy to the PC, it should appear as a Joystick, and a serial port device will also appear.

Edit the code.py file on the Itsy and change debug from False to True for extra info from the serial port

At every restart of the ubs-rc code, set the TX to full FWD, REV, L and R and the unit will self-calibrate the extents.

Itsy can be bought from here: https://www.adafruit.com/product/3800

The "code.py" is the "regular" version that is, at the moment, the preferred version for the Trinket M0.  I don't currently have a Trinket M0 to test the other features that have been added since the inception.  This should work with regular receivers, and sanwa receivers in NOR and SHR mode.

The "test_3channel.py" version is the same as "code.py" but has support for a third channel.  The third input from the receiver is to port A2.  To use it, copy it to the CIRCUITPY usb-drive and rename it to "cody.py".  You may want to rename the old "code/py" to something else in case you want to put the old version back.  This should work with regular receivers, and sanwa receivers in NOR and SHR mode.  This version hasn't been tested on the Trinket M0, but seems to work just fine on the ItsyBotsy M4.
On my TX at least - I chose to have SW1 funcion as an on-off switch. For this I had to go to SYSTEM->ASSIGN-> and set 
 - SW1 -> AUX1
 - LEVER -> AUX2
 - DIAL -> AUX2

![sw1](https://github.com/colzilla/usb-rc/blob/master/images/IMG_8998.jpg)

![lever](https://github.com/colzilla/usb-rc/blob/master/images/IMG_8999.jpg)

![dial](https://github.com/colzilla/usb-rc/blob/master/images/IMG_9001.jpg)

The "usb_rc_sanwa_ssr.py" version is the same as "test_3channel.py" but modified to deal with the sanwa SSR mode.  It will not work with a "normal" receiver.  Note that the sanwa TX/RX must be bound in SSR mode.  From my testing it's possible to change the TX from SHR to SSR on the menu, but it will still be in SHR mode until rebind.
In addition to the 4x response rate that SSR offers, this version samples only 1 pulse.  The previous versions sample 5 pulses which was introduced to lighten the CPU load.  The ItsyBitsy seems fine with the high rate.

It's advisable to set pretty much everything on the TX to default - especially the EPAs, to convey 100% of travel to the RX.

At every power-up or reset of the board, it needs to re-learn the endpoints of the TX/RX combination, which is achieded by turning fell-left, full-right, full-throttle, full-brake a few times.  Once this is done, use the Windows Joystick Calibration wizard to have Windows learn the center-points.  It's intentionally done this way to allow for both 50/50 and 70/30 throttle/brake splits on the transmitter, and still keep one set of instructions :)

Good luck - and enjoy!

NOR Mode:
![NORmode](https://github.com/colzilla/usb-rc/blob/master/images/IMG_9004.jpg)

SHR (Sanwa High Rate) Mode:
![SHRmode](https://github.com/colzilla/usb-rc/blob/master/images/IMG_9003.jpg)

SSR (Sanwa Super Rate) Mode:
![SSRmode](https://github.com/colzilla/usb-rc/blob/master/images/IMG_9002.jpg)

