# usb-rc_sanwa_ssr_4ch

AdaFruit Trinket M0 and ItsyBitsy M4 USB adapter for RC receivers

Install

1. Copy the "adafruit_hid" folder and the "code.py" file to the CIRCUITPY folder on your AdaFruit ItsyBitsy
2. Connect the RX GND to the "G" pin on the Itsy
3. Connect the RX 5V to the "USB" pin on the Itsy
4. Connect the RX CH1 to the "A3" pin on the Itsy
5. Connect the RX CH2 to the "A4" pin on the Itsy

See the images folder for pictures.
![itsy_a](https://github.com/colzilla/usb-rc/blob/master/images/IMG_9031.jpg)
![itsy_b](https://github.com/colzilla/usb-rc/blob/master/images/IMG_9034.jpg)
![sanwa_rxa](https://github.com/colzilla/usb-rc/blob/master/images/IMG_9035.jpg)
![sanwa_rxb](https://github.com/colzilla/usb-rc/blob/master/images/IMG_9036.jpg)

Connect the itsy to the PC, it should appear as a Joystick, and a serial port device will also appear.

Edit the code.py file on the Itsy and change debug from False to True for extra info from the serial port.

Itsy can be bought from here: https://www.adafruit.com/product/3800

The "usb_rc_sanwa_ssr_4ch.py" version supports 4x Sanwa SSR channels ONLY.  It cannot "see" NOR or SHR signals.  

Power to the RX is delivered from the VHi and GND pins.

The inputs to the ItsyBitsy are remapped so the port-number matches the channel number:
 -Channel 1 -> A1
 -Channel 2 -> A2
 -Channel 3 -> A3
 -Channel 4 -> A4
 
To use it, copy the .py file to the CIRCUITPY usb-drive and rename it to "cody.py".  You may want to rename the old "code.py" to something else in case you want to put the old version back.  This version hasn't been tested on the Trinket M0, but seems to work just fine on the ItsyBitsy M4.

On my TX at least - I chose to have SW1 funcion as an on-off switch. For this I had to go to SYSTEM->ASSIGN-> and set 
 - SW1 -> AUX1
 - SW3 -> AUX1
 - LEVER -> ---
 - DIAL -> ---

In addition to the 4x response rate that SSR offers, this version samples only 1 pulse.  The previous versions sample 5 pulses which was introduced to lighten the CPU load.  The ItsyBitsy seems fine with the high rate.

It's advisable to set pretty much everything on the TX to default - especially the EPAs, to convey 100% of travel to the RX.

At every power-up or reset of the board, it needs to re-learn the endpoints of the TX/RX combination, which is achieded by turning fell-left, full-right, full-throttle, full-brake a few times.  Once this is done, use the Windows Joystick Calibration wizard to have Windows learn the center-points.  It's intentionally done this way to allow for both 50/50 and 70/30 throttle/brake splits on the transmitter, and still keep one set of instructions :)

Good luck - and enjoy!

SSR (Sanwa Super Rate) Mode:
![SSRmode](https://github.com/colzilla/usb-rc/blob/master/images/IMG_9002.jpg)

