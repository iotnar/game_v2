# This Python file uses the following encoding: utf-8
import os, sys
import pygame as pg
import sys


pg.init()

screen_width = 840
screen_height = 566
screen = pg.display.set_mode([screen_width, screen_height])
zastavka = pg.image.load('zastavka2.jpg').convert()

clock = pg.time.Clock()
FPS = 120
pg.font.init()
f = pg.font.Font('ConsolaMono.ttf', 15)

def nadpis_text(y, i, x, messeg,messeg1):
   while i < int(len(messeg)):
                text1 = f.render(str(messeg1), False, (49, 168, 77))
                screen.blit(text1, (10, y))
                pg.display.update()
                #klik.play(0, 0, 0).set_volume(0.05)
                text = f.render(str(messeg[i]), True, (49, 168, 77))
                screen.blit(text, (100 + x, y))
                pg.display.update()
                pg.time.wait(120)
                i += 1
                x += 13

def update_ck_1():
    i = 0
    x = 13
    f = pg.font.Font('D3Digitalism-BWwG.ttf', 15)
    messeg1 = "18F000__:"
    messeg = "Здравствуйте Александр"
    #priv1.play(0, 0, 0)
    nadpis_text(10, i, x, messeg, messeg1)
    pg.time.wait(300)
    messeg = "приветствую вас в нашем доме"
    #priv2.play(0, 0, 0)
    nadpis_text(30, i, x, messeg, messeg1)
    pg.time.wait(300)
    messeg = "предлагаю малость развлечься"
    #priv3.play(0, 0, 0)
    nadpis_text(50, i, x, messeg, messeg1)
    #screen.blit(zastavka, (0, 0))
    pg.display.update()