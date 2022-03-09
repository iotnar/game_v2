# This Python file uses the following encoding: utf-8
import os, sys

import pygame as pg
import first
import zagruzka
import end
import game


def run():
    zagruzka.update_zagruzka(1, 0)
    print('яяяяя111')



"""загрузка музыки"""
pg.mixer.pre_init(44100, -16, 2, 512)
pg.mixer.music.load('elektro.wav')
#pg.mixer.music.play()
#zag = pg.mixer.Sound('vkluchenie.wav')
#klik = pg.mixer.Sound('klik.wav')
#priv1 = pg.mixer.Sound('voxworker-voice-file.mp3')
#priv2 = pg.mixer.Sound('fraza2.mp3')
#priv3 = pg.mixer.Sound('fraza3.mp3')

"""экран загрузки"""
pg.init()


run()
end.off()