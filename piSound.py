__author__ = 'clipo'

import pygame
import sys
import os
from subprocess import call

pygame.mixer.init()
pygame.mixer.music.load("./sounds/trickortreat.wav")
pygame.mixer.music.play()
call(["ls", "-l"])
os.system("aplay ./sounds/trickortreat.wav")
