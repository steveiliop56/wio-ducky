# License : GPLv2.0
# copyright (c) 2023  Dave Bailey
# Author: Dave Bailey (dbisu, @daveisu)
# Wio terminal addition: Steve Iliopoulos (steveiliop56, @steveiliop56)


import supervisor

import time
import digitalio
from board import *
import board
from duckyinpython import *


# sleep at the start to allow the device to be recognized by the host computer
time.sleep(0.5)

# turn off automatically reloading when files are written to the wio
# supervisor.disable_autoreload()
supervisor.runtime.autoreload = False


progStatus = False
progStatus = getProgrammingStatus()
print("Programming status (setup mode):", progStatus)

if(progStatus == False):
    print("Finding payload...")
    # not in setup mode, inject the payload
    payload = selectPayload(startup=True)
    print(f"Running {payload}.")
    runScript(payload)

    print("Done!")
else:
    print("Update your payload.")

async def main_loop():
    global button1

    button_task = asyncio.create_task(monitor_buttons(button1))
    wio_led_task = asyncio.create_task(blink_wio_led(led))
    await asyncio.gather(wio_led_task, button_task)

asyncio.run(main_loop())
