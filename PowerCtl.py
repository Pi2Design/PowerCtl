#!/usr/bin/python
# The purpose of this script is to power down the Pi properly through software
# when the volume knob switch is turned to the off position

# import RPi.GPIO for proper gpio access
from subprocess import call
import time
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("ERROR importing RPi.GPIO! Please make sure it is installed and you have superuser privileges")

# This defines a loop to keep the script running
def loop():
    while True:
        time.sleep(10)

# This defines a function to run when interrupt is called
def shutdown(pin):
    call(["/var/www/command/rune_shutdown", "poweroff"], shell=False)
    call("poweroff", shell=False)

GPIO.setmode(GPIO.BCM)
# We drive GPIO 22 high to keep the power on
# After the Pi is shutdown via software it will cease to be driven and will be pulled low.
GPIO.setup(22,GPIO.OUT, initial=GPIO.HIGH)
# Pin 24 will be HIGH when the volume switch is in the 'Powered OFF' position
GPIO.setup(24,GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(24, GPIO.RISING, callback=shutdown, bouncetime=200)

loop()
