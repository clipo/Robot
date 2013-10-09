__author__ = 'clipo'

import RPi.GPIO as GPIO
from time import sleep
import LPD8806
import time
import random
from subprocess import call
import getch
import os
from Adafruit_VCNL4000 import VCNL4000
import time
from Adafruit_PWM_Servo_Driver import PWM

pwm = PWM(0x40, debug=True)
vcnl = VCNL4000(0x13)
led = LPD8806.strand()
GPIO.setmode(GPIO.BCM)
os.system("amixer set PCM -- -2200")
os.system("amixer cset numid=3 1")
servoMin = 150  # Min pulse length out of 4096
servoMax = 4000  # Max pulse length out of 4096

directory = "./sounds/"
sounds=["affirmative2.wav",
"beepboopboopboop2.wav",
"blip2.wav","error.wav","hello.wav","imrobot2.wav","lowbeepboop.wav","robotcom.wav","trickortreat.wav",
"affirmative.wav","beepboopboopboop.wav","blip.wav","gimmesomecandy.wav","iamrobot.wav","imrobot3.wav","merrychristmas.wav","robots.wav","trortr.wav",
"beepbeepbeepbeep.wav","beepboop.wav","candycorn.wav","greatpumpkin.wav","imarobot4.wav","imrobot.wav","peep2.wav","scifi.wav",
"beepbeep.wav","bleep.wav","countdwn.wav","happyhalloween.wav","imarobot5.wav","peep.wav","trickortreat2.wav"]


# GPIO 23 set up as input. It is pulled up to stop false signals
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
time_stamp = time.time()
counter =0

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)

def quit():
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit

# this will run in another thread when our event is detected
def button1():
    global time_stamp       # put in to debounce
    time_now = time.time()
    global counter
    if (time_now - time_stamp and counter==0) >= 0.3:
        counter=1
        print "Beep 1\n"
        alist=["happyhalloween.wav","merrychristmas.wav","candycorn.wav","greatpumpkin.wav"]
        #alist=["happyhalloween.wav"]
        rand=random.randrange(0,len(alist))
        file="aplay ./sounds/"+alist[rand]
        os.system(file)
    time_stamp = time_now
    counter=0

# this will run in another thread when our event is detected
def button2():
    global time_stamp       # put in to debounce
    time_now = time.time()
    global counter
    if (time_now - time_stamp and counter==0) >= 0.5:
        counter =1
        print "Beep 2\n"
        blist=["beepboopboopboop2.wav","blip2.wav","lowbeepboop.wav","beepboopboopboop.wav.wav","blip.wav","beepbeepbeepbeep.wav","beepboop.wav","countdwn.wav"]
        #blist=["beepboopboop2.wav"]
        rand=random.randrange(0,len(blist))
        file="aplay ./sounds/"+blist[rand]
        os.system(file)
    time_stamp = time_now
    counter = 0

# this will run in another thread when our event is detected
def button3():
    global time_stamp       # put in to debounce
    global counter
    time_now = time.time()
    if (time_now - time_stamp and counter==0) >= 0.5:
        counter = 1
        print "Beep 3\n"
        clist=["affirmative2.wav","error.wav","hello.wav","imrobot.wav","imrobot2.wav","robotcom.wav","affirmative.wav","iamrobot.wav","imrobot2","imrobot3.wav","robots.wav","imarobot5.wav","imarobot4.wav"]
        #clist=["imrobot3.wav"]
        rand=random.randrange(0,len(clist))
        file="aplay ./sounds/"+clist[rand]
        os.system(file)
    time_stamp = time_now
    counter = 0

# this will run in another thread when our event is detected
def button4():
    global time_stamp       # put in to debounce
    time_now = time.time()
    global counter
    if (time_now - time_stamp and counter==0) >= 1:
        counter = 1
        print "Beep 4\n"
        rand=random.randrange(0,len(sounds))
        file="aplay ./sounds/"+sounds[rand]
        os.system(file)
    time_stamp = time_now
    counter=0

# this will run in another thread when our event is detected
def button5():
    global time_stamp       # put in to debounce
    time_now = time.time()
    global counter
    if (time_now - time_stamp and counter==0) >= 0.5:
        counter=1
        print "Beep 5\n"
        dlist=["trortr.wav","trickortreat2.wav","trickortreat.wav","gimmesomecandy.wav"]
        #dlist=["trickortreat3.wav"]
        rand=random.randrange(0,len(dlist))
        file="aplay ./sounds/"+dlist[rand]
        os.system(file)

        try:
            stateValue
        except NameError:
            global stateValue
            stateValue=0
        if stateValue == 0:
            pwm.setPWM(0,0,servoMin)
            stateValue=1
        else:
            pwm.setPWM(0,0,servoMax)
            stateValue=0
    time_stamp = time_now
    counter =0

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
GPIO.add_event_detect(17, GPIO.FALLING, callback=lambda x: button1(), bouncetime=2000)
GPIO.add_event_detect(22, GPIO.FALLING, callback=lambda x: button2(), bouncetime=2000)
GPIO.add_event_detect(23, GPIO.FALLING, callback=lambda x: button3(), bouncetime=2000)
GPIO.add_event_detect(25, GPIO.FALLING, callback=lambda x: button4(), bouncetime=500)
GPIO.add_event_detect(24, GPIO.FALLING, callback=lambda x: button5(), bouncetime=2000)
stateValue=1
while True:
    print "Data from proximity sensor", vcnl.read_proximity()
    for i in range(5):
        led.fill(255, 0, 0)
        led.update()
        print "Data from proximity sensor", vcnl.read_proximity()
        sleep(0.3)
        led.fill(0, 255, 0)
        led.update()
        print "Data from proximity sensor", vcnl.read_proximity()
        sleep(0.3)
        led.fill(0, 0, 255)
        led.update()
        print "Data from proximity sensor", vcnl.read_proximity()
        sleep(0.3)
   # for i in range(300):
   #     led.wheel()
   #     led.update()

