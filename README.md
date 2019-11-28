# usb-rc
AdaFruit Trinket M0 and ItsyBitsy M4 USB adapter for RC receivers

Install

1. Copy the "adafruit_hid" folder and the "code.py" file to the CIRCUITPY folder on your AdaFruit ItsyBitsy
2. Connect the RX GND to the "G" pin on the Itsy
3. Connect the RX 5V to the "USB" pin on the Itsy
4. Connect the RX CH1 to the "A3" pin on the Itsy
5. Connect the RX CH2 to the "A4" pin on the Itsy

See the images folder for pictures.

Connect the itsy to the PC, it should appear as a Joystick, and a serial port device will also appear.

Edit the code.py file on the Itsy and change debug from False to True for extra info from the serial port

At every restart of the ubs-rc code, set the TX to full FWD, REV, L and R and the unit will self-calibrate the extents.


