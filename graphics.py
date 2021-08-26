from typing import runtime_checkable
import pygame

WIDTH, HEIGHT = 700, 900
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    

    pygame.quit()