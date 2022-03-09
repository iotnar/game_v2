# This Python file uses the following encoding: utf-8
import os, sys
import pygame as pg
import sys
from random import randint
import first

pg.init()
screen_width = 840
screen_height = 566
screen = pg.display.set_mode([screen_width, screen_height])
zastavka = pg.image.load('zastavka2.jpg').convert()
clock = pg.time.Clock()
def off():
    screen.blit(zastavka, (0, 0))
    pg.display.update()
    pg.time.wait(900)
    sys.exit()