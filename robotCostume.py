__author__ = 'clipo'

import RPi.GPIO as GPIO
from time import sleep
import LPD8806
import time
import random
from subprocess import call
import getch

led = LPD8806.strand()
GPIO.setmode(GPIO.BCM)

directory = "./sounds/"
sounds=["affirmative2.wav",
"beepboopboopboop2.wav",
"blip2.wav","error.wav","hello.wav","imrobot2.wav","lowbeepboop.wav","robotcom.wav","trickortreat.wav",
"affirmative.wav","beepboopboopboop.wav","blip.wav","gimmesomecandy.wav","iamrobot.wav","imrobot3.wav","merrychristmas.wav","robots.wav","trortr.wav",
"beepbeepbeepbeep.wav","beepboop.wav","candycorn.wav","greatpumpkin.wav","imarobot4.wav","imrobot.wav","peep2.wav","scifi.wav",
"beepbeep.wav","bleep.wav","countdwn.wav","happyhalloween.wav","imarobot5.wav","peep.wav","trickortreat3.wav"]


# GPIO 23 set up as input. It is pulled up to stop false signals
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

global stateValue
stateValue=0

def quit():
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit

# this will run in another thread when our event is detected
def button1(channel):
    print "Beep 1\n"
    rand=random.randrange(0,5)
    alist=["happy.wav","happyhalloween.wav","merrychristmas.wav","candycorn.wav","greatpumpkin.wav"]	
    file="./sounds/"+alist[rand]
    call(file)

# this will run in another thread when our event is detected
def button2(channel):
    print "Beep 2\n"
    rand=random.randrange(0,9)
    blist=["beepboopboop2.wav","blip2.wav","lowbeepboop.wav","beepboopboopboop.wav","blip.wav","beepbeepbeepbeep.wav","beepbeep.wav","beep.wav","countdwn.wav"]	
    file="./sounds/"+blist[rand]
    call(file)

# this will run in another thread when our event is detected
def button3(channel):
    print "Beep 3\n"
    rand=random.randrange(0,10)
    clist=["affirmative2.wav","error.wav","hello.wav","imrobot2.wav","robotcom.wav","affirmative.wav","iamrobot.wav","iamrobot3.wav","robots.wav","iamrobot5.wav"]	
    file="./sounds/"+clist[rand]
    call(file)


# this will run in another thread when our event is detected
def button4(channel):
    print "Beep 4\n"
    rand=random.randrange(0,len(list))
    file="./sounds/"+list[rand]
    call(file)

# this will run in another thread when our event is detected
def button5(channel):
    print "Beep 5\n"
    rand=random.randrange(0,4)
    dlist=["trortr.wav","trickortreat3.wav","trickortreat.wav","gimmesomecandy.wav"]	
    file="./sounds/"+dlist[rand]
    call(file)

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
GPIO.add_event_detect(20, GPIO.FALLING, callback=lambda x: button1(), bouncetime=2000)
GPIO.add_event_detect(21, GPIO.FALLING, callback=lambda x: button2(), bouncetime=2000)
GPIO.add_event_detect(22, GPIO.FALLING, callback=lambda x: button3(), bouncetime=2000)
GPIO.add_event_detect(23, GPIO.FALLING, callback=lambda x: button4(), bouncetime=2000)
GPIO.add_event_detect(24, GPIO.FALLING, callback=lambda x: button5(), bouncetime=2000)

def keycheck():
    ch = getch.getch()
    if ch == '\x03':
        quit()
    elif ch=='q':
        quit()

while True:
    keycheck()
    for i in range(5):
        keycheck()
        led.fill(255, 0, 0)
        led.update()
        sleep(0.3)
        led.fill(0, 255, 0)
        led.update()
        sleep(0.3)
        led.fill(0, 0, 255)
        led.update()
        sleep(0.3)
    keycheck()
    for i in range(300):
        keycheck()
        led.wheel()
        led.update()
    keycheck()

