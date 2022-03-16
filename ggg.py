import pygame
import controls
from gun import Gun
from pygame.sprite import Group
from random import randint
from score import Score
#pygame.mixer.pre_init
#pygame.init()
#pygame.mixer.music.load('Wav/start_muzik.mp3')
#pygame.mixer.music.play()

gun_shot = pygame.mixer.Sound('Wav/vyistrel-s-vibratsiey.wav')
vzruv = pygame.mixer.Sound('Wav/vzruv.wav')





def run_game(screen):


    pygame.init()
    zastavka = pygame.image.load('zastavka2.jpg').convert()
    #screen = pygame.display.set_mode((500, 600))
    #pygame.display.set_caption("Заруба")
    clock = pygame.time.Clock()
    FPS = 120
    bg_color = (0, 0, 0)

    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    score = Score(screen)
    controls.bild_army(screen, inos)

    #рисуем экран приветствия
    #controls.update_first(screen)
    #clock.tick(FPS)
    while True: # рисуем экран игры
        controls.events(screen, gun,  bullets, gun_shot)
        gun.updategun()
        controls.update(zastavka, screen, gun, inos, bullets, score)
        controls.update_bullets(screen, bullets, inos, vzruv, score)
        controls.update_inos(inos)
        clock.tick(FPS)

#run_game()


