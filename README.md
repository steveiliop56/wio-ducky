<h1 align="center" Wio Terminal-ducky</h1>

<div align="center">
  <strong>Make a cheap but powerful USB Rubber Ducky with a Wio Terminal</strong>
</div>

<div align="center">
  <h6>Warning! This is a fork of dbisu Wio Terminal-ducky so the code is not mine, it is just modified for the Wio terminal!</h6>
  <h6>Warning! Currently nothing works because I am working in the source duckyinpython to fucntion on the wio terminal so this repo is just for testing.</h6>
</div>

## Install

Install and have your USB Rubber Ducky working in less than 5 minutes.

1. Clone the repo to get a local copy of the files. `git clone https://github.com/steveiliop56 Wio-ducky.git`

2. Download [CircuitPython for the Wio Terminal](https://circuitpython.org/board/seeeduino Wio_terminal/). *Updated to 8.0.0  

3. Plug the device into a USB port and enter bootloader mode by sliding the power button down very fast. It will show up as a removable media device named `ARDUINO`.

4. Copy the downloaded `.uf2` file to the root of the Wio Terminal (`ARDUINO`). The device will reboot and after a second or so, it will reconnect as `CIRCUITPY`.

5. Download `adafruit-circuitpython-bundle-8.x-mpy-YYYYMMDD.zip` [here](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/latest) and extract it outside the device.

6. Navigate to `lib` in the recently extracted folder and copy `adafruit_hid` to the `lib` folder on your Raspberry Pi Wio Terminal.

7. Copy `adafruit_debouncer.mpy` and `adafruit_ticks.mpy` to the `lib` folder on your Raspberry Pi Wio Terminal.

8. Copy `asyncio` to the `lib` folder on your Wio Terminal.

9. Copy `adafruit_wsgi` to the `lib` folder on your Wio Terminal.

10. Copy `boot.py` from your clone to the root of your Wio Terminal.

11. Copy `duckyinpython.py`, `code.py`, `webapp.py`, `wsgiserver.py` to the root folder of the Wio Terminal.

12. *If you want to use a web server* Create the file `secrets.py` in the root of the Wio Terminal W. This contains the AP name and password to be created by the Wio Terminal.  
`secrets = { 'ssid' : "BadAPName", 'password' : "badpassword" }`

1.  Find a script [here](https://github.com/hak5/usbrubberducky-payloads) or [create your own one using Ducky Script](https://docs.hak5.org/hak5-usb-rubber-ducky/ducky-script-basics/hello-world) and save it as `payload.dd` in the Wio Terminal. Currently, wio-ducky only supports DuckScript 1.0, not 3.0.

2.  Be careful, if your device isn't in [setup mode](#setup-mode), the device will reboot and after half a second, the script will run.

3.  **Please note:** by default Wio Terminal will not show as a USB drive!

### Wio Terminal Web Service
The Wio Terminal AP defaults to ip address `192.168.4.1`.  You should be able to find the webservice at `http://192.168.4.1:80`  

The following endpoints are available on the webservice:
```
/
/new
/ducky
/edit/<filename>
/write/<filename>
/run/<filename>
```

API endpoints
```
/api/run/<filenumber>
```

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
 Wio Terminal: The default mode is USB mass storage enabled.


### Multiple payloads

Multiple payloads can be stored on the Wio Terminal.  
To select a payload, you have to firstly press and hold the left button and you will be greeted with a menu where you can run the payloads: 

## Useful links and resources

### Installation Tool

[steveiliop56](https://github.com/steveilop56) Created a tool to convert a blank RPi Wio Terminal to a ducky.  
You can find the tool [here](https://github.com/steveiliop56/pyducky) **(no longer maintained)**

### Docs

[CircuitPython](https://circuitpython.readthedocs.io/en/6.3.x/README.html)

[CircuitPython HID](https://learn.adafruit.com/circuitpython-essentials/circuitpython-hid-keyboard-and-mouse)

[Ducky Script](https://github.com/hak5darren/USB-Rubber-Ducky/wiki/Duckyscript)

### Video tutorials

Pico-ducky tutorial by **NetworkChuck**](https://www.youtube.com/watch?v=e_f9p-_JWZw) **(Same as wio terminal)**

[USB Rubber Ducky playlist by **Hak5**](https://www.youtube.com/playlist?list=PLW5y1tjAOzI0YaJslcjcI4zKI366tMBYk)
