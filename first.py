# This Python file uses the following encoding: utf-8
import os, sys
import pygame as pg
import end
import ggg

pg.init()

screen_width = 840
screen_height = 566
screen = pg.display.set_mode([screen_width, screen_height])
zastavka = pg.image.load('zastavka2.jpg').convert()
start1 = pg.image.load('start.png').convert_alpha()
start2 = pg.image.load('start2.png').convert_alpha()
clock = pg.time.Clock()
FPS = 120
pg.font.init()
f = pg.font.Font('ConsolaMono.ttf', 15)

"""инициализируем спрайт для кнопок"""
class Button(pg.sprite.Sprite):
    def __init__(self, screen, text, color ):
        self.screen = screen
        self.font = pg.font.Font('ConsolaMono.ttf', 15)
        self.text = self.font.render(text,False,color)

    def output(self,x, y):
        """отрисовка кнопки"""
        self.screen.blit(self.text, (x, y))



def nadpis_text(y, i, x, messeg,messeg1):
   while i < int(len(messeg)):
                text1 = f.render(str(messeg1), False, (49, 168, 77))
                screen.blit(text1, (10, y))
                pg.display.update()
                #klik.play(0, 0, 0).set_volume(0.05)
                text = f.render(str(messeg[i]), False, (49, 168, 77))
                screen.blit(text, (100 + x, y))
                pg.display.update()
                pg.time.wait(120)
                i += 1
                x += 13

def update_ck_1():
    color1 = (49, 168, 77)
    color2 = (255, 177, 70)

    a = color1
    b = color2
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
    z = 0
    while z == 0:
        button1 = Button(screen, 'START GAME', a)
        button2 = Button(screen, 'QUIT GAME', b)

        for q in pg.event.get():
            if q.type == pg.QUIT:
                sys.exit()

            button1.output(100, 400)
            button2.output(400, 400)
            #screen.blit(start, (100, 400))
            pg.display.update()

            if q.type == pg.KEYDOWN:
                if q.key == pg.K_a:
                    a = color2
                    b = color1

                    pg.display.update

                if q.key == pg.K_d:
                    a = color1
                    b = color2

                    pg.display.update
                if q.key == pg.K_SPACE and a == color2:
                    print('stop')#sys.exit()
                    ggg.run_game(screen)

                elif q.key == pg.K_SPACE and a == color1:
                    print('start')
                    end.off()

