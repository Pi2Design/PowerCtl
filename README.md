# PowerCtl
The CSB503HTA includes a power switch on its volume knob, and circuitry to allow the Pi to shutdown gracefully when the switch is clicked off. This Python script sets up the proper GPIOs to enable this behavior.

Clone this repository to your home directory and then edit /etc/rc.local to run the file on boot by adding:

  /usr/bin/python /home/YOUR_USERNAME/PowerCtl/PowerCtl.py &

before exit 0. YOUR_USERNAME will be the user who's home directory the script has been cloned into. It may be pi for raspbian, volumio for volumio, or a user name you have added. The ampersand at the end of the line is very important. It allows this script to run in the background. If it is not there, the login prompt may be blocked.
