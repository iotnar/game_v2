# This Python file uses the following encoding: utf-8
import os, sys

import pygame as pg
import first
import zagruzka
import end
import ggg

pg.mixer.pre_init(44100, -16, 2, 512)
pg.mixer.music.load('elektro.wav')

pg.init()

screen_width = 840
screen_height = 566
screen = pg.display.set_mode([screen_width, screen_height])
zastavka = pg.image.load('zastavka2.jpg').convert()
screen.blit(zastavka, (0, 0))
pg.display.update()

def run():
    while True:

        zagruzka.update_zagruzka(1, 0)
        print('яяяяя111')
        first.update_ck_1()
        ggg.run_game(screen)



"""загрузка музыки"""

#pg.mixer.music.play()
#zag = pg.mixer.Sound('vkluchenie.wav')
#klik = pg.mixer.Sound('klik.wav')
#priv1 = pg.mixer.Sound('voxworker-voice-file.mp3')
#priv2 = pg.mixer.Sound('fraza2.mp3')
#priv3 = pg.mixer.Sound('fraza3.mp3')

"""экран загрузки"""



run()
