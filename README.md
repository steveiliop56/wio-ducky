<h1 align="center" Wio Terminal-ducky</h1>

<div align="center">
  <strong>Make a cheap but powerful USB Rubber Ducky with a Wio Terminal</strong>
</div>

<div align="center">
  <h6>Warning! This is a fork of dbisu pico-ducky so the code is not mine, it is just modified for the Wio terminal!</h6>
</div>

## Install

Install and have your USB Rubber Ducky working in less than 5 minutes.

1. Clone the repo to get a local copy of the files. `git clone https://github.com/steveiliop56/wio-ducky.git`

2. Download [CircuitPython for the Wio Terminal](https://circuitpython.org/board/seeeduino_wio_terminal/). *Updated to 8.0.5  

3. Plug the device into a USB port and enter bootloader mode by sliding the power button down very fast 2 times. It will show up as a removable media device named `ARDUINO`.

4. Copy the downloaded `.uf2` file to the root of the Wio Terminal (`ARDUINO`). The device will reboot and after a second or so, it will reconnect as `CIRCUITPY`.

5. Download `adafruit-circuitpython-bundle-8.x-mpy-YYYYMMDD.zip` [here](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/latest) and extract it outside the device.

6. Navigate to `lib` in the recently extracted folder and copy `adafruit_hid` to the `lib` folder on your Raspberry Pi Wio Terminal.

7. Copy `adafruit_debouncer.mpy` and `adafruit_ticks.mpy` to the `lib` folder on your Wio Terminal.

8. Copy `asyncio` to the `lib` folder on your Wio Terminal.

9. Download both `adafruit-circuitpython-display-shapes-8.x-mpy-2.6.0.zip` from [here](https://github.com/adafruit/Adafruit_CircuitPython_Display_Shapes/releases) and 
the `adafruit-circuitpython-display-text-8.x-mpy-2.28.1.zip` from [here](https://github.com/adafruit/Adafruit_CircuitPython_Display_Text/releases) extract them and copy the `adafruit_display_shapes` and the `adafruit_display_text` to the `lib` folder of your wio terminal.

10. Copy `boot.py` from your clone to the root of your Wio Terminal.

11. Copy `duckyinpython.py`, `code.py`, `screen_menu.py`, to the root folder of the Wio Terminal.

**Note:** You can skip installing all the requirements manually by just running the `circup` command and you will find the requirements inside the `requirements.txt` file.
### Payloads 

1.  Find a script [here](https://github.com/hak5/usbrubberducky-payloads) or [create your own one using Ducky Script](https://docs.hak5.org/hak5-usb-rubber-ducky/ducky-script-basics/hello-world) and save it as `payload.dd` in the Wio Terminal `payloads` folder. You can copy the 4 default ones from your clone of the repository. Currently, wio-ducky only supports DuckScript 1.0, not 3.0.

2.  Be careful, if your device isn't in [setup mode](#setup-mode), the device will reboot and after half a second, the script will run.

3.  **Please note:** by default Wio Terminal will not show as a USB drive!

### Setup mode 

To edit the payload, enter setup mode by pressing the right top button, this will stop the Wio wio-ducky from injecting the payload in your own machine.

### USB enable/disable mode 

If you need the wio-ducky to not show up as a USB mass storage device for stealth, follow these instructions.  
- Enter setup mode.    
- Copy your payload script to the wio-ducky.  
- Disconnect the Wio Terminal from your host PC.
- Connect a jumper wire between pin 6 (`GND`) and pin 13 (`D0`).  
This will prevent the Wio Terminal-ducky from showing up as a USB drive when plugged into the target computer.  
- Remove the jumper and reconnect to your PC to reprogram.  
 **Wio Terminal:** The default mode is USB mass storage enabled.

![Enable Storage Wiring](https://user-images.githubusercontent.com/106091011/230954488-d0b1f9bb-09fe-4169-92f2-5fff513782a0.png)

### Screen enable/disable mode

If you need the wio-ducky's display to not show logs in the display, follow these instructions.  
- Disconnect the Wio Terminal from your host PC.
- Connect a jumper wire between pin 4 (`+5V`) and pin 15 (`D1`).  
This will prevent the Wio Terminal-ducky from showing up as a USB drive when plugged into the target computer.  
- Remove the jumper and reconnect to your PC to reprogram.  
 **Wio Terminal:** The default mode is USB mass storage enabled.

![Disable Screen Wiring](https://user-images.githubusercontent.com/106091011/230954611-9575da69-0164-4db4-b0ad-d58454557500.png)

### Multiple payloads

Multiple payloads can be stored on the Wio Terminal.  
To select a payload, you have to firstly press and hold the left button and you will be greeted with a menu where you can run the payloads stored in the `payloads` folder. The payloads should be named with these 4 names: `payload.dd` (which is the default one), `payload1.dd`, `payload2.dd`, `payload3.dd`. Here is a picture of how the menu looks:

![Payload Selector Menu](https://user-images.githubusercontent.com/106091011/230953940-75acc450-ff7e-4919-b3fe-297a8ee2b792.jpg)

### Self destroy mode

If you hold the middle button while the wio terminal is booting it will erase everything in the flash and appear as a simple `CIRCUITPY` device without anyone knowing about the payloads that it stored.

## Useful links and resources

### Plug and Play

In the [releases](https://github.com/steveiliop56/wio-ducky/releases) page you can find a file named `wio-ducky-plug-and-play.zip` which you can just unzip in your wio terminal copy your payloads and it's ready!

### Installation Tool

[steveiliop56](https://github.com/steveilop56) Created a tool to convert a blank Wio Terminal to a ducky.  
You can find the tool [here](https://github.com/steveiliop56/pyducky) **(no longer maintained and not working with wio-ducky)**

### Docs

[CircuitPython](https://circuitpython.readthedocs.io/en/6.3.x/README.html)

[CircuitPython HID](https://learn.adafruit.com/circuitpython-essentials/circuitpython-hid-keyboard-and-mouse)

[Ducky Script](https://github.com/hak5darren/USB-Rubber-Ducky/wiki/Duckyscript)

### Video tutorials

Pico-ducky tutorial by [**NetworkChuck**](https://www.youtube.com/watch?v=e_f9p-_JWZw) **(Same as wio terminal)**

[USB Rubber Ducky playlist by **Hak5**](https://www.youtube.com/playlist?list=PLW5y1tjAOzI0YaJslcjcI4zKI366tMBYk)
