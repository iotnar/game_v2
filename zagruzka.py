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
FPS = 120
count = 0
pg.font.init()
f = pg.font.Font('D3Digitalism-BWwG.ttf', 50)



centr_x_s = screen_width/2-50
centr_y_s = screen_height/2-25

def update_zagruzka(i, count):
       while i <= 100:
          if count <= 100:
                r = randint(1, 3)
                text = f.render((str(count)+' %'), True, (49, 168, 77))
                screen.blit(text, (centr_x_s, centr_y_s))
                pg.display.update()
                pg.time.wait(110)
                screen.blit(zastavka, (0, 0))
                pg.display.update()
                i+= 1
                count += r
                pg.time.wait(60)
          else:
             i = 110
             screen.blit(f.render('100 %', True, (49, 168, 77)), (centr_x_s, centr_y_s))
             pg.display.update()
             pg.time.wait(600)
             screen.blit(zastavka, (0, 0))
             pg.display.update()

