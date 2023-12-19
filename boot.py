# License : GPLv2.0
# copyright (c) 2023  Dave Bailey
# Author: Dave Bailey (dbisu, @daveisu)
# Wio terminal addition: Stavros (steveiliop56, @steveiliop56)

from board import *
from duckyinpython import getStorageStatus, getScreenStatus
import board
import digitalio
import storage
import displayio
import os
import sys

storageStatus = False
storageStatus = getStorageStatus()

if storageStatus == True:
    storage.disable_usb_drive()
    print("Disabling USB drive.")
else:
    # normal boot
    print("USB drive enabled.")

screenStatus = False
screenStatus = getScreenStatus()

if screenStatus == True:
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

