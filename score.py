# This Python file uses the following encoding: utf-8
import pygame



class Score():

    def __init__(self, screen, stats):
        """инициалезируем статистику"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.score_count = stats
        self.font = pygame.font.Font('ConsolaMono.ttf', 60)
        self.text = self.font.render(str(self.score_count), True, (49, 168, 80))



    def gun_minus(self):
        """счетчик жизни пушки"""
        self.gun_life = 2

    def draw(self):
        self.screen.blit(self.text, (650, 200))
        self.score_plus()

    def score_plus(self):
        self.score_count += 10