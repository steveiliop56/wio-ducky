# License : GPLv2.0
# copyright (c) 2023  Dave Bailey
# Author: Dave Bailey (dbisu, @daveisu)
# Wio terminal addition: Stavros (steveiliop56, @steveiliop56)

from duckyinpython import *
from screen_menu import *
import supervisor
import time


# sleep at the start to allow the device to be recognized by the host computer
time.sleep(1)

# turn off automatically reloading when files are written to the wio
# supervisor.disable_autoreload()
supervisor.runtime.autoreload = False


progStatus = False
progStatus = getProgrammingStatus()
print("Programming status (setup mode): ", progStatus)

displayMenu = False
displayMenu = getMenuStatus()
print("Display menu (visual selector): ", displayMenu)

storageStatus = False
storageStatus = getStorageStatus()
print("Storage status (enable storage): ", storageStatus)

if progStatus == False:
    if displayMenu == True:
        payload = display_menu()
        if payload == 0:
            runScript("payloads/payload.dd")
        else:
            runScript(f"payloads/payload{str(payload)}.dd")
    else:
        print(f"Running default payload.")
        runScript("payloads/payload.dd")
        print("Done!")
else:
    if storageStatus == True:
        print("Cannot enable programming mode, storage disabled!")
        print("The script will exit now!")
        exit()
    else:
        print("Update your payload.")
