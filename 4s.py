import pygame
import sys
from gun import Gun
from gun7 import Gun7

def run():
    pygame.init()
    screen = pygame.display.set_mode((1420,800))
    pygame.display.set_caption("Космические защитники")
    bg_color=(112, 250, 110)
    gun = Gun(screen)
    gun7 = Gun7(screen)
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        gun.output()
        gun7.output()
        pygame.display.flip()       
run()
