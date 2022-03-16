# This Python file uses the following encoding: utf-8
import pygame
import controls
from gun import Gun
from pygame.sprite import Group
from random import randint




pygame.mixer.pre_init
gun_shot = pygame.mixer.Sound('Wav/vyistrel-s-vibratsiey.wav')
vzruv = pygame.mixer.Sound('Wav/vzruv.wav')
i = 1

def run_game(screen):
    pygame.mixer.music.load('Wav/start_muzik.mp3')
    pygame.mixer.music.play(-1)
    zastavka = pygame.image.load('zastavka3.jpg').convert()
    pygame.display.set_caption("заруба")
    clock = pygame.time.Clock()
    FPS = 120
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.bild_army(screen, inos)
    clock.tick(FPS)
    while True:
        controls.events(screen, gun,  bullets, gun_shot)
        gun.updategun()
        controls.update(zastavka, screen, gun, inos, bullets)
        controls.update_bullets(screen, bullets, inos, vzruv)
        controls.update_inos(inos)
        clock.tick(FPS)

#run_game()


