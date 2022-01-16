import pygame


class Gun7():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/terminator-t-800-robot.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

    def output(self):
        """рисование пушки"""
        self.screen.blit(self.image, self.rect)
