# License : GPLv2.0
# copyright (c) 2023  Dave Bailey
# Author: Dave Bailey (dbisu, @daveisu)
# Wio terminal addition: Steve Iliopoulos (steveiliop56, @steveiliop56)

from board import *
import board
import digitalio
import storage
import displayio
import os
import sys

noStoragePin = digitalio.DigitalInOut(board.D0)
noStoragePin.switch_to_input(pull=digitalio.Pull.UP)
noStorageStatus = noStoragePin.value

# If D0 is not connected, it will default to being pulled high (True)
# If D0 is connected to GND, it will be low (False)

if noStorageStatus == True:
    # don't show USB drive to host PC
    storage.disable_usb_drive()
    print("Disabling USB drive.")
else:
    # normal boot
    print("USB drive enabled.")

noScreenPin = digitalio.DigitalInOut(board.D1)
noScreenPin.switch_to_input(pull=digitalio.Pull.DOWN)
noScreenStatus = noScreenPin.value

# If D1 is not connected, it will default to being pulled high (False)
# If D1 is connected to 5V, it will be low (True)

if noScreenStatus == True:
    # don't enable the display output
    displayio.release_displays()
    print("Disabling the screen.")
else:
    # normal boot
    print("Screen enabled.")


# If the middle switch is not connected, it will default to being pulled high (False)
# If the middle switch is pressed, it will be low (True)

destroy_pin = digitalio.DigitalInOut(board.BUTTON_2) # defaults to input
destroy_pin.pull = digitalio.Pull.UP   # turn on internal pull-up resistor

if destroy_pin.value != True:
    print("Activating self destroy...")
    storage.erase_filesystem()
else:
    pass

