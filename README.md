# ros_mpl3115a2

A ROS node for communicating with the [MPL3115A2](https://www.adafruit.com/product/1893) temperature, barometer, and altimeter sensor.

## Description

The node communicates with the MPL3115A2 via i2c on the Raspberry Pi using Adafruit's Circuit Python library: https://learn.adafruit.com/using-mpl3115a2-with-circuitpython.  The i2c address is preset to 0x60 which is the default.  This is configurable if needed.  The data is stored in the following:

* Temperature (C): `mpl3115a2/temperature`
* Pressure (Pascals): `mpl3115a2/pressure`
* Altimeter (m): `mpl3115a2/altimeter`

## Installation Instructions

* Enable i2c
  ```
  sudo apt-get install i2c-tools
  i2cdetect -l
  ```
* Add `i2c-devl` to boot with `sudo nano /etc/modules-load.d/modules.conf`
* Install wiringpi `sudo apt install wiringpi`
* Connect i2c devices to Sparkfun Qwiic hat and run `i2cdetect -y 1` to identify channels
* Install Circuit Python: https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi
* Install driver for MPL3115A2 Baro/Temp/Alt Sensor: `sudo pip3 install adafruit-circuitpython-mpl3115a2`.

## Running the Node

* Option 1: `rosrun ros_mpl3115a2 talker.py` 
* Option 2: `roslaunch launches/pitemp.launch`
## Tested Setup

It should work on other versions but Python 3 is a requirement.

* Platform: Raspberry Pi 4
* OS: Ubuntu MATE 20.04
* ROS: Noetic
* Python: 3.8.5

