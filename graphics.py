import pygame

pygame.init()
WIDTH, HEIGHT = 700, 900
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

WHITE = (255, 255, 255)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        
        WINDOW.fill(WHITE)
        pygame.display.update()
