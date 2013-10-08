__author__ = 'clipo'

import RPi.GPIO as GPIO
from time import sleep
import LPD8806
import time
import random
from subprocess import call
import getch
import os

led = LPD8806.strand()
GPIO.setmode(GPIO.BCM)
os.system("amixer set PCM -- -2200")
os.system("amixer cset numid=3 1")

directory = "./sounds/"
sounds=["affirmative2.wav",
"beepboopboopboop2.wav",
"blip2.wav","error.wav","hello.wav","imrobot2.wav","lowbeepboop.wav","robotcom.wav","trickortreat.wav",
"affirmative.wav","beepboopboopboop.wav","blip.wav","gimmesomecandy.wav","iamrobot.wav","imrobot3.wav","merrychristmas.wav","robots.wav","trortr.wav",
"beepbeepbeepbeep.wav","beepboop.wav","candycorn.wav","greatpumpkin.wav","imarobot4.wav","imrobot.wav","peep2.wav","scifi.wav",
"beepbeep.wav","bleep.wav","countdwn.wav","happyhalloween.wav","imarobot5.wav","peep.wav","trickortreat3.wav"]


# GPIO 23 set up as input. It is pulled up to stop false signals
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)



def quit():
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit

# this will run in another thread when our event is detected
def button1():
    print "Beep 1\n"
    alist=["happyhalloween.wav","merrychristmas.wav","candycorn.wav","greatpumpkin.wav"]	
    rand=random.randrange(0,len(alist))
    file="aplay ./sounds/"+alist[rand]
    os.system(file)

# this will run in another thread when our event is detected
def button2():
    print "Beep 2\n"
    blist=["beepboopboop2.wav","blip2.wav","lowbeepboop.wav","beepboopboopboop.wav","blip.wav","beepbeepbeepbeep.wav","beepbeep.wav","beep.wav","countdwn.wav"]	
    rand=random.randrange(0,len(blist))
    file="aplay ./sounds/"+blist[rand]
    os.system(file)

# this will run in another thread when our event is detected
def button3():
    print "Beep 3\n"
    clist=["affirmative2.wav","error.wav","hello.wav","imrobot2.wav","robotcom.wav","affirmative.wav","iamrobot.wav","iamrobot3.wav","robots.wav","iamrobot5.wav"]	
    rand=random.randrange(0,len(clist))
    file="aplay ./sounds/"+clist[rand]
    os.system(file)

# this will run in another thread when our event is detected
def button4():
    print "Beep 4\n"
    rand=random.randrange(0,len(sounds))
    file="aplay ./sounds/"+sounds[rand]
    os.system(file)

# this will run in another thread when our event is detected
def button5():
    print "Beep 5\n"
    dlist=["trortr.wav","trickortreat3.wav","trickortreat.wav","gimmesomecandy.wav"]	
    rand=random.randrange(0,len(dlist))
    file="aplay ./sounds/"+dlist[rand]
    os.system(file)

    try:
        stateValue
    except NameError:
        global stateValue
        stateValue=0
    if stateValue == 0:
        for angle in range(0, 180):
            setServo(angle)
        stateValue=1
    else:
        for angle in range(0, 180):
            setServo(180 - angle)
        stateValue=0

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
#GPIO.add_event_detect(17, GPIO.FALLING, callback=lambda x: button1(), bouncetime=2000)
#GPIO.add_event_detect(22, GPIO.FALLING, callback=lambda x: button2(), bouncetime=2000)
GPIO.add_event_detect(23, GPIO.FALLING, callback=lambda x: button3(), bouncetime=2000)
GPIO.add_event_detect(24, GPIO.FALLING, callback=lambda x: button4(), bouncetime=500)
GPIO.add_event_detect(25, GPIO.FALLING, callback=lambda x: button5(), bouncetime=2000)
stateValue=1
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

