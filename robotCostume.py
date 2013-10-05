__author__ = 'clipo'

import RPi.GPIO as GPIO
from time import sleep
import LPD8806
import pygame
import time


led = LPD8806.strand()
GPIO.setmode(GPIO.BCM)

# GPIO 23 set up as input. It is pulled up to stop false signals
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pygame.mixer.init()
global state
state=0

def quit():
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit

# this will run in another thread when our event is detected
def button1(channel):
    print "Beep 1\n"
    pygame.mixer.music.load("iamarobot.wav")
    pygame.mixer.music.play()

# this will run in another thread when our event is detected
def button2(channel):
    print "Beep 2\n"
    pygame.mixer.music.load("beepboop.wav")
    pygame.mixer.music.play()

# this will run in another thread when our event is detected
def button3(channel):
    print "Beep 3\n"
    pygame.mixer.music.load("happy.wav")
    pygame.mixer.music.play()

# this will run in another thread when our event is detected
def button4(channel):
    print "Beep 4\n"
    pygame.mixer.music.load("beep.wav")
    pygame.mixer.music.play()

# this will run in another thread when our event is detected
def button5(channel):
    print "Beep 5\n"
    pygame.mixer.music.load("trortr.wav")
    pygame.mixer.music.play()
    if state == 0:
        for angle in range(0, 180):
            setServo(angle)
        state=1
    else:
        for angle in range(0, 180):
            setServo(180 - angle)
        state=0

def set(property, value):
    try:
        f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
        f.write(value)
        f.close()
    except:
        print("Error writing to: " + property + " value: " + value)

def setServo(angle):
    set("servo", str(angle))

# The GPIO.add_event_detect() line below set things up so that
# when a rising edge is detected on port 24, regardless of whatever
# else is happening in the program, the function "my_callback" will be run
# It will happen even while the program is waiting for
# a falling edge on the other button.
GPIO.add_event_detect(20, GPIO.RISING, callback=button1)
GPIO.add_event_detect(21, GPIO.RISING, callback=button2)
GPIO.add_event_detect(22, GPIO.RISING, callback=button3)
GPIO.add_event_detect(23, GPIO.RISING, callback=button4)
GPIO.add_event_detect(24, GPIO.RISING, callback=button5)


while True:
    for i in range(5):
        led.fill(255, 0, 0)
        led.update()
        sleep(0.3)
        led.fill(0, 255, 0)
        led.update()
        sleep(0.3)
        led.fill(0, 0, 255)
        led.update()
        sleep(0.3)
    for i in range(300):
        led.wheel()
        led.update()