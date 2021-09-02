import pygame
from Board import *

# from rough import *

boardObj = Board()
boardObj.set_board(1)
############## MAKE SURE LINES END AT COL 80?
# board = [  [7, 0, 8, 0, 0, 0, 0, 0 ,0], 
#                         [0, 0, 0, 0, 0, 0, 0, 0 ,0], 
#                         [0, 0, 0, 0, 0, 0, 0, 0 ,0],
#                         [0, 0, 0, 0, 0, 0, 0, 0 ,0],
#                         [0, 0, 0, 0, 0, 0, 0, 0 ,0], 
#                         [0, 0, 0, 0, 0, 0, 0, 0 ,0],
#                         [0, 0, 0, 0, 0, 0, 0, 0 ,0],
#                         [0, 0, 0, 0, 0, 0, 0, 0 ,0],
#                         [0, 0, 0, 0, 0, 0, 0, 9 ,3]  ]
pygame.init()
WIDTH, HEIGHT = 680, 780
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def draw_window():
    WINDOW.fill(WHITE)  # white area is (650 x 650) 
    # bottom bar
    pygame.draw.rect(WINDOW, BLACK, (0, HEIGHT-100, WIDTH, 100))
    
    # border:
    border_width = 10
    box_width = WIDTH - 2*border_width #650
    grid = pygame.transform.scale(pygame.image.load('grid.png'), (660, 660))#(WIDTH-border_width*2-2, HEIGHT-border_width*2-100-2))
    WINDOW.blit(grid, (border_width, border_width))
    pygame.draw.rect(WINDOW, RED, (0, 0, border_width, HEIGHT-100)) #left
    pygame.draw.rect(WINDOW, RED, (WIDTH-border_width, 0, border_width, HEIGHT-100)) #right
    pygame.draw.rect(WINDOW, RED, (0, 0, WIDTH, border_width)) #top
    pygame.draw.rect(WINDOW, RED, (0, HEIGHT-100-border_width, WIDTH, border_width)) #bottom

    # pygame.draw.line(WINDOW, GREEN, (0, 20), (14, 20))
    # pygame.draw.line(WINDOW, GREEN, (665, 20), (679, 20))

    # # big squares  (each square is 214 x 214)
    # bigline_width = 3
    # bigsquare_width = (box_width - 2*bigline_width) / 3  #214
    # pygame.draw.line(WINDOW, BLACK, (bigsquare_width+border_width, border_width), (bigsquare_width+border_width, box_width+border_width), bigline_width) #214 = (650-8)/3
    # pygame.draw.line(WINDOW, BLACK, (bigsquare_width*2+border_width+bigline_width, border_width), (bigsquare_width*2+border_width+bigline_width, box_width+border_width), bigline_width)
    # pygame.draw.line(WINDOW, BLACK, (border_width, bigsquare_width+border_width), (box_width+border_width, bigsquare_width+border_width), bigline_width)
    # pygame.draw.line(WINDOW, BLACK, (border_width, bigsquare_width*2+border_width+bigline_width), (box_width+border_width, bigsquare_width*2+border_width+bigline_width), bigline_width)
    # #### small squares (71.333 x 71.333)
    # # small vertical lines
    # smallsquare_width = bigsquare_width/3  #71.333
    # pygame.draw.line(WINDOW, BLUE, (smallsquare_width+border_width, border_width), (smallsquare_width+border_width, box_width+border_width))
    # pygame.draw.line(WINDOW, BLUE, (smallsquare_width*2+border_width, border_width), (smallsquare_width*2+border_width, box_width+border_width))
    # pygame.draw.line(WINDOW, BLUE, (border_width+bigsquare_width+smallsquare_width, border_width), (border_width+bigsquare_width+smallsquare_width, border_width+box_width))
    # pygame.draw.line(WINDOW, BLUE, (border_width+bigsquare_width+smallsquare_width*2+1, border_width), (border_width+bigsquare_width+smallsquare_width*2+1, border_width+box_width))
    # pygame.draw.line(WINDOW, BLUE, (border_width+bigsquare_width*2+bigline_width*2+smallsquare_width, border_width), (border_width+bigsquare_width*2+bigline_width*2+smallsquare_width, border_width+box_width))
    # pygame.draw.line(WINDOW, BLUE, (border_width+bigsquare_width*2+bigline_width*2+smallsquare_width*2+1, border_width), (border_width+bigsquare_width*2+bigline_width*2+smallsquare_width*2+1, border_width+box_width))
    # # small horizontal lines
    # pygame.draw.line(WINDOW, BLUE, (border_width, smallsquare_width+border_width), (border_width+box_width, smallsquare_width+border_width))
    # pygame.draw.line(WINDOW, BLUE, (border_width, smallsquare_width*2+border_width), (border_width+box_width, smallsquare_width*2+border_width))
    # pygame.draw.line(WINDOW, BLUE, (border_width, border_width+bigsquare_width+smallsquare_width), (border_width+box_width, border_width+bigsquare_width+smallsquare_width))
    # pygame.draw.line(WINDOW, BLUE, (border_width, border_width+bigsquare_width+smallsquare_width*2+1), (border_width+box_width, border_width+bigsquare_width+smallsquare_width*2+1))
    # pygame.draw.line(WINDOW, BLUE, (border_width, border_width+bigsquare_width*2+bigline_width*2+smallsquare_width), (border_width+box_width, border_width+bigsquare_width*2+bigline_width*2+smallsquare_width))
    # pygame.draw.line(WINDOW, BLUE, (border_width, border_width+bigsquare_width*2+bigline_width*2+smallsquare_width*2+1), (border_width+box_width, border_width+bigsquare_width*2+bigline_width*2+smallsquare_width*2+1))
    
    nums_font = pygame.font.SysFont('calibri', 50, False)

    for i in range(boardObj.size):
        for j in range(boardObj.size):
            # if (i==0):
            if boardObj.board[i][j] != 0:
                nums_text = nums_font.render(str(boardObj.board[i][j]), 1, BLUE)
                if (2<j<6):
                    # WINDOW.blit(nums_text, (17+24+j*72, 15+14+i*72))
                    w = 17+24+j*72
                    h = 15+14+i*72
                elif (5<j):
                    # WINDOW.blit(nums_text, (19+24+j*72.2, 15+14+i*72))
                    w = 19+24+j*72.2
                    h = 15+14+i*72
                else:
                    # WINDOW.blit(nums_text, (12+24+j*72.2, 15+14+i*72))
                    w = 12+24+j*72.2
                    h = 15+14+i*72

                if 2<i<6:
                    h += 4
                elif 5<i:
                    h += 7
                
                WINDOW.blit(nums_text, (w, h))
                
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)  # controls the speed of this while loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        draw_window()
        
main()
# print(pygame.font.get_fonts())