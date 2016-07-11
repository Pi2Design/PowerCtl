# PowerCtl
The CSB503HTA includes a power switch on its volume knob, and circuitry to allow the Pi to shutdown gracefully when the switch is clicked off. This Python script sets up the proper GPIOs to enable this behavior. 
BCM GPIO 22 is used to hold the power on and BCM GPIO 24 is used to sense the power switch.
This script has been tested on PI2 running Volumio.

Clone this repository to your home directory and test it by running
  
  sudo python PowerCtl/PowerCtl.py
  
When the volume knob is turned to the power off position, the Pi should initiate a software shutdown and stay powered until the shutdown is complete. 

Some systems may not include the python RPi.GPIO library by default.

To install you can try:
  sudo apt-get update
  sudo apt-get install python-dev python-rpi.gpio
If that fails then try:
  sudo apt-get install python-dev python-pip
  sudo bash
  pip install RPi.GPIO

Once everything works then edit /etc/rc.local to run the file on boot by adding:

  /usr/bin/python /home/YOUR_USERNAME/PowerCtl/PowerCtl.py &

before exit 0. YOUR_USERNAME will be the user into whose home directory the script has been cloned. It may be pi for raspbian, volumio for volumio, or a user name you have added. The ampersand at the end of the line is very important. It allows this script to run in the background. If it is not there, the login prompt may be blocked.
