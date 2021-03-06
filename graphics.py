import pygame
from Board import *

boardObj = Board()
starting_slots = boardObj.set_board(1)

############## MAKE SURE LINES END AT COL 80?

pygame.init()
WIDTH, HEIGHT = 680, 780
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

FPS = 60
z = -1
square_clicked = False
border_width = 10
boxes = [((border_width+5, border_width+5+70), (border_width+5, border_width+5+70)),
    ((border_width+78, border_width+78+73), (border_width+5, border_width+5+71)),
    ((border_width+9+70*2, border_width+9+70*2+70), (border_width+5, border_width+5+70)),
    ((border_width+8+72*3, border_width+8+72*3+70), (border_width+5, border_width+5+70)),
    ((border_width+6+72*4, border_width+6+72*4+73), (border_width+5, border_width+5+71)),
    ((border_width+7+72*5, border_width+7+72*5+70), (border_width+5, border_width+5+70)),
    ((border_width+10+72*6, border_width+10+72*6+70), (border_width+5, border_width+5+70)),
    ((border_width+9+72*7, border_width+9+72*7+73), (border_width+5, border_width+5+71)),
    ((border_width+10+72*8, border_width+10+72*8+70), (border_width+5, border_width+5+70)),

    ((border_width+5, border_width+5+71), (border_width+5+70, border_width+5+70+73)),
    ((border_width+5+71, border_width+5+71+73), (border_width+5+70, border_width+5+70+73)),
    ((border_width+5+71*2+2, border_width+5+71*2+2+71), (border_width+5+70, border_width+5+70+73)),
    ((border_width+5+72*3+3, border_width+5+71*3+3+71), (border_width+5+70, border_width+5+70+73)),
    ((border_width+5+72*4+1, border_width+5+72*4+1+73), (border_width+5+70, border_width+5+70+73)),
    ((border_width+5+72*5+2, border_width+5+72*5+2+71), (border_width+5+70, border_width+5+70+73)),
    ((border_width+5+72*6+5, border_width+5+72*6+5+71), (border_width+5+70, border_width+5+70+73)),
    ((border_width+5+72*7+4, border_width+5+72*7+4+73), (border_width+5+70, border_width+5+70+73)),
    ((border_width+5+72*8+5, border_width+5+72*8+5+71), (border_width+5+70, border_width+5+70+73)),

    ((border_width+5, border_width+5+70), (border_width+8+70*2, border_width+8+70*2+70)),
    ((border_width+5+71, border_width+5+71+73), (border_width+8+70*2, border_width+8+70*2+71)),
    ((border_width+5+72*2, border_width+5+72*2+70), (border_width+8+70*2, border_width+8+70*2+70)),
    ((border_width+5+72*3+3, border_width+5+72*3+3+70), (border_width+8+70*2, border_width+8+70*2+70)),
    ((border_width+5+72*4+1, border_width+5+72*4+1+73), (border_width+8+70*2, border_width+8+70*2+71)),
    ((border_width+5+72*5+2, border_width+5+72*5+2+70), (border_width+8+70*2, border_width+8+70*2+70)),
    ((border_width+5+72*6+5, border_width+5+72*6+5+70), (border_width+8+70*2, border_width+8+70*2+70)),
    ((border_width+5+72*7+4, border_width+5+72*7+4+73), (border_width+8+70*2, border_width+8+70*2+71)),
    ((border_width+5+72*8+5, border_width+5+72*8+5+70), (border_width+8+70*2, border_width+8+70*2+70)),

    ((border_width+5, border_width+5+70), (border_width+5+70*3+8, border_width+5+70*3+8+70)),
    ((border_width+5+71, border_width+5+71+73), (border_width+5+70*3+8, border_width+5+70*3+8+71)),
    ((border_width+5+72*2, border_width+5+72*2+70), (border_width+5+70*3+8, border_width+5+70*3+8+70)),
    ((border_width+5+72*3+3, border_width+5+72*3+3+70), (border_width+5+70*3+8, border_width+5+70*3+8+70)),
    ((border_width+5+72*4+1, border_width+5+72*4+1+73), (border_width+5+70*3+8, border_width+5+70*3+8+71)),
    ((border_width+5+72*5+2, border_width+5+72*5+2+70), (border_width+5+70*3+8, border_width+5+70*3+8+70)),
    ((border_width+5+72*6+5, border_width+5+72*6+5+70), (border_width+5+70*3+8, border_width+5+70*3+8+70)),
    ((border_width+5+72*7+4, border_width+5+72*7+4+73), (border_width+5+70*3+8, border_width+5+70*3+8+71)),
    ((border_width+5+72*8+5, border_width+5+72*8+5+70), (border_width+5+70*3+8, border_width+5+70*3+8+70)),

    ((border_width+5, border_width+5+71), (border_width+5+70*4+9, border_width+5+70*4+9+73)),
    ((border_width+5+71, border_width+5+71+73), (border_width+5+70*4+9, border_width+5+70*4+9+73)),
    ((border_width+5+72*2+2, border_width+5+72*2+2+71), (border_width+5+70*4+9, border_width+5+70*4+9+73)),
    ((border_width+5+72*3+3, border_width+5+72*3+3+71), (border_width+5+70*4+9, border_width+5+70*4+9+73)),
    ((border_width+5+72*4+1, border_width+5+72*4+1+73), (border_width+5+70*4+9, border_width+5+70*4+9+73)),
    ((border_width+5+72*5+2, border_width+5+72*5+2+71), (border_width+5+70*4+9, border_width+5+70*4+9+73)),
    ((border_width+5+72*6+5, border_width+5+72*6+5+71), (border_width+5+70*4+9, border_width+5+70*4+9+73)),
    ((border_width+5+72*7+4, border_width+5+72*7+4+73), (border_width+5+70*4+9, border_width+5+70*4+9+73)),
    ((border_width+5+72*8+5, border_width+5+72*8+5+71), (border_width+5+70*4+9, border_width+5+70*4+9+73)),

    ((border_width+5, border_width+5+70), (border_width+8+70*5+9, border_width+8+70*5+9+70)),
    ((border_width+5+71, border_width+5+71+73), (border_width+8+70*5+9, border_width+8+70*5+9+71)),
    ((border_width+5+72*2, border_width+5+72*2+70), (border_width+8+70*5+9, border_width+8+70*5+9+70)),
    ((border_width+5+72*3+3, border_width+5+72*3+3+70), (border_width+8+70*5+9, border_width+8+70*5+9+70)),
    ((border_width+5+72*4+1, border_width+5+72*4+1+73), (border_width+8+70*5+9, border_width+8+70*5+9+71)),
    ((border_width+5+72*5+2, border_width+5+72*5+2+70), (border_width+8+70*5+9, border_width+8+70*5+9+70)),
    ((border_width+5+72*6+5, border_width+5+72*6+5+70), (border_width+8+70*5+9, border_width+8+70*5+9+70)),
    ((border_width+5+72*7+4, border_width+5+72*7+4+73), (border_width+8+70*5+9, border_width+8+70*5+9+71)),
    ((border_width+5+72*8+5, border_width+5+72*8+5+70), (border_width+8+70*5+9, border_width+8+70*5+9+70)),

    ((border_width+5, border_width+5+70), (border_width+5+70*6+18, border_width+5+70*6+18+70)),
    ((border_width+5+71, border_width+5+71+73), (border_width+5+70*6+18, border_width+5+70*6+18+70)),
    ((border_width+5+72*2, border_width+5+72*2+70), (border_width+5+70*6+18, border_width+5+70*6+18+70)),
    ((border_width+5+72*3+3, border_width+5+72*3+3+70), (border_width+5+70*6+18, border_width+5+70*6+18+70)),
    ((border_width+5+72*4+1, border_width+5+72*4+1+73), (border_width+5+70*6+18, border_width+5+70*6+18+70)),
    ((border_width+5+72*5+2, border_width+5+72*5+2+70), (border_width+5+70*6+18, border_width+5+70*6+18+70)),
    ((border_width+5+72*6+5, border_width+5+72*6+5+70), (border_width+5+70*6+18, border_width+5+70*6+18+70)),
    ((border_width+5+72*7+4, border_width+5+72*7+4+73), (border_width+5+70*6+18, border_width+5+70*6+18+70)),
    ((border_width+5+72*8+5, border_width+5+72*8+5+70), (border_width+5+70*6+18, border_width+5+70*6+18+70)),

    ((border_width+5, border_width+5+71), (border_width+5+70*7+18, border_width+5+70*7+18+73)),
    ((border_width+5+71, border_width+5+71+73), (border_width+5+70*7+18, border_width+5+70*7+18+71)),
    ((border_width+5+72*2, border_width+5+72*2+71), (border_width+5+70*7+18, border_width+5+70*7+18+73)),
    ((border_width+5+72*3+3, border_width+5+72*3+3+71), (border_width+5+70*7+18, border_width+5+70*7+18+73)),
    ((border_width+5+72*4+1, border_width+5+72*4+1+73), (border_width+5+70*7+18, border_width+5+70*7+18+71)),
    ((border_width+5+72*5+2, border_width+5+72*5+2+71), (border_width+5+70*7+18, border_width+5+70*7+18+73)),
    ((border_width+5+72*6+5, border_width+5+72*6+5+71), (border_width+5+70*7+18, border_width+5+70*7+18+73)),
    ((border_width+5+72*7+4, border_width+5+72*7+4+73), (border_width+5+70*7+18, border_width+5+70*7+18+71)),
    ((border_width+5+72*8+5, border_width+5+72*8+5+71), (border_width+5+70*7+18, border_width+5+70*7+18+73)),

    ((border_width+5, border_width+5+70), (border_width+5+70*8+19, border_width+5+70*8+19+70)),
    ((border_width+5+71, border_width+5+71+73), (border_width+5+70*8+19, border_width+5+70*8+19+71)),
    ((border_width+5+72*2, border_width+5+72*2+70), (border_width+5+70*8+19, border_width+5+70*8+19+70)),
    ((border_width+5+72*3+3, border_width+5+72*3+3+70), (border_width+5+70*8+19, border_width+5+70*8+19+70)),
    ((border_width+5+72*4+1, border_width+5+72*4+1+73), (border_width+5+70*8+19, border_width+5+70*8+19+71)),
    ((border_width+5+72*5+2, border_width+5+72*5+2+70), (border_width+5+70*8+19, border_width+5+70*8+19+70)),
    ((border_width+5+72*6+5, border_width+5+72*6+5+70), (border_width+5+70*8+19, border_width+5+70*8+19+70)),
    ((border_width+5+72*7+4, border_width+5+72*7+4+73), (border_width+5+70*8+19, border_width+5+70*8+19+71)),
    ((border_width+5+72*8+5, border_width+5+72*8+5+70), (border_width+5+70*8+19, border_width+5+70*8+19+70)),
    ]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def draw_window(mouse_click):
    global z, square_clicked
    WINDOW.fill(WHITE)  # white area is (650 x 650) 
    # bottom bar
    pygame.draw.rect(WINDOW, BLACK, (0, HEIGHT-100, WIDTH, 100))
    
    # border:
    # border_width = 10
    box_width = WIDTH - 2*border_width #650
    # grid = pygame.transform.scale(pygame.image.load('mygrid.png'), (660, 660))#(WIDTH-border_width*2-2, HEIGHT-border_width*2-100-2))
    WINDOW.blit(pygame.image.load('mygridnew.png'), (border_width, border_width)) #put grid for 1st param 
    pygame.draw.rect(WINDOW, RED, (0, 0, border_width, HEIGHT-100)) #left
    pygame.draw.rect(WINDOW, RED, (WIDTH-border_width, 0, border_width, HEIGHT-100)) #right
    pygame.draw.rect(WINDOW, RED, (0, 0, WIDTH, border_width)) #top
    pygame.draw.rect(WINDOW, RED, (0, HEIGHT-100-border_width, WIDTH, border_width)) #bottom

    
    ###### THIS IS TO HIGHLIGHT A BOX
    small_box_width = 69

    boxes_starting_corners = [(border_width+5, border_width+5), 
    (border_width+7+69, border_width+5),
    (border_width+9+70*2, border_width+5),
    (border_width+8+72*3, border_width+5), 
    (border_width+6+72*4, border_width+5), 
    (border_width+7+72*5, border_width+5), 
    (border_width+10+72*6, border_width+5), 
    (border_width+9+72*7, border_width+5), 
    (border_width+10+72*8, border_width+5),

    (border_width+5, border_width+5+70), 
    (border_width+5+71, border_width+5+70), 
    (border_width+5+71*2+2, border_width+5+70), 
    (border_width+5+72*3+3, border_width+5+70), 
    (border_width+5+72*4+1, border_width+5+70), 
    (border_width+5+72*5+2, border_width+5+70), 
    (border_width+5+72*6+5, border_width+5+70), 
    (border_width+5+72*7+4, border_width+5+70), 
    (border_width+5+72*8+5, border_width+5+70),

    (border_width+5, border_width+9+70*2), 
    (border_width+5+71, border_width+8+70*2), 
    (border_width+5+72*2, border_width+9+70*2), 
    (border_width+5+72*3+3, border_width+9+70*2), 
    (border_width+5+72*4+1, border_width+8+70*2), 
    (border_width+5+72*5+2, border_width+9+70*2), 
    (border_width+5+72*6+5, border_width+9+70*2), 
    (border_width+5+72*7+4, border_width+8+70*2), 
    (border_width+5+72*8+5, border_width+9+70*2),


    (border_width+5, border_width+5+70*3+8), 
    (border_width+5+71, border_width+5+70*3+8),
    (border_width+5+72*2, border_width+5+70*3+8),
    (border_width+5+72*3+3, border_width+5+70*3+8), 
    (border_width+5+72*4+1, border_width+5+70*3+8), 
    (border_width+5+72*5+2, border_width+5+70*3+8), 
    (border_width+5+72*6+5, border_width+5+70*3+8), 
    (border_width+5+72*7+4, border_width+5+70*3+8), 
    (border_width+5+72*8+5, border_width+5+70*3+8),


    (border_width+5, border_width+5+70*4+9), 
    (border_width+5+71, border_width+5+70*4+9), 
    (border_width+5+71*2+2, border_width+5+70*4+9), 
    (border_width+5+72*3+3, border_width+5+70*4+9), 
    (border_width+5+72*4+1, border_width+5+70*4+9), 
    (border_width+5+72*5+2, border_width+5+70*4+9), 
    (border_width+5+72*6+5, border_width+5+70*4+9), 
    (border_width+5+72*7+4, border_width+5+70*4+9), 
    (border_width+5+72*8+5, border_width+5+70*4+9),


    (border_width+5, border_width+8+70*5+9), 
    (border_width+5+71, border_width+8+70*5+9), 
    (border_width+5+71*2+2, border_width+8+70*5+9), 
    (border_width+5+72*3+3, border_width+8+70*5+9), 
    (border_width+5+72*4+1, border_width+8+70*5+9), 
    (border_width+5+72*5+2, border_width+8+70*5+9), 
    (border_width+5+72*6+5, border_width+8+70*5+9), 
    (border_width+5+72*7+4, border_width+8+70*5+9), 
    (border_width+5+72*8+5, border_width+8+70*5+9),


    (border_width+5, border_width+5+70*6+18), 
    (border_width+5+71, border_width+5+70*6+18),
    (border_width+5+72*2, border_width+5+70*6+18),
    (border_width+5+72*3+3, border_width+5+70*6+18), 
    (border_width+5+72*4+1, border_width+5+70*6+18), 
    (border_width+5+72*5+2, border_width+5+70*6+18), 
    (border_width+5+72*6+5, border_width+5+70*6+18), 
    (border_width+5+72*7+4, border_width+5+70*6+18), 
    (border_width+5+72*8+5, border_width+5+70*6+18),

    (border_width+5, border_width+5+70*7+18), 
    (border_width+5+71, border_width+5+70*7+18),
    (border_width+5+72*2, border_width+5+70*7+18),
    (border_width+5+72*3+3, border_width+5+70*7+18), 
    (border_width+5+72*4+1, border_width+5+70*7+18), 
    (border_width+5+72*5+2, border_width+5+70*7+18), 
    (border_width+5+72*6+5, border_width+5+70*7+18), 
    (border_width+5+72*7+4, border_width+5+70*7+18), 
    (border_width+5+72*8+5, border_width+5+70*7+18),

    (border_width+5, border_width+5+70*8+19), 
    (border_width+5+71, border_width+5+70*8+19),
    (border_width+5+72*2, border_width+5+70*8+19),
    (border_width+5+72*3+3, border_width+5+70*8+19), 
    (border_width+5+72*4+1, border_width+5+70*8+19), 
    (border_width+5+72*5+2, border_width+5+70*8+19), 
    (border_width+5+72*6+5, border_width+5+70*8+19), 
    (border_width+5+72*7+4, border_width+5+70*8+19), 
    (border_width+5+72*8+5, border_width+5+70*8+19)
    ]
    
    if mouse_click:
        z = find_square_clicked(mouse_click, False)

    # match mouse click with a square
    visitedfirst2ifs = False  # this is if we visit the first 2 if statements but dont wanna go to the elif/else
    if z % 3 == 1 and not (54 < z < 64):
        boxw = 73
        boxh = 71
        visitedfirst2ifs = True
    if z == 55 or z == 58 or z == 61 or z == 1 or z == 4 or z == 7 or\
        z == 73 or z == 76 or z == 79:
        boxw = 73
        boxh = 70
        visitedfirst2ifs = True
    if z == 10 or z == 13 or z == 16 or z == 37 or z == 40 or z == 43:
        boxw = 73
        boxh = 73
    elif 8 < z < 18 or 35 < z < 45 or 62 < z < 72 and not visitedfirst2ifs:
        boxw = 70
        boxh = 73
    elif not visitedfirst2ifs:
        boxw = 70
        boxh = 70
    if z != -1:
        if square_clicked:
            pygame.draw.rect(WINDOW, (155, 155, 155), (boxes_starting_corners[z][0], boxes_starting_corners[z][1], boxw, boxh))
            
    nums_font = pygame.font.SysFont('calibri', 50, False)

    for i in range(boardObj.size):
        for j in range(boardObj.size):
            if boardObj.board[i][j] != 0:
                nums_text = nums_font.render(str(boardObj.board[i][j]), 1, BLUE)
                if (2<j<6):
                    w = 15+24+j*72
                    h = 15+14+i*72
                elif (5<j):
                    w = 17+24+j*72.2
                    h = 15+14+i*72
                else:
                    w = 12+24+j*72.2
                    h = 15+14+i*72

                if 2<i<6:
                    h += 4
                elif 5<i:
                    h += 7
                
                WINDOW.blit(nums_text, (w, h))
                
    pygame.display.update()



def main():
    global square_clicked
    clock = pygame.time.Clock()
    click = False
    

    run = True
    while run:
        clock.tick(FPS)  # controls the speed of this while loop
        mouse_pos = pygame.mouse.get_pos()  #this is a tuple
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    click_pos = mouse_pos
                    draw_window(mouse_pos)
                    # print(mouse_pos)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

            if event.type == pygame.KEYDOWN and square_clicked:
                if event.key == pygame.K_1:
                    index = find_square_clicked(click_pos, True)
                    if (index//9, index%9) not in starting_slots:
                        boardObj.board[index//9][index%9] = 1

                if event.key == pygame.K_2:
                    index = find_square_clicked(click_pos, True)
                    if (index//9, index%9) not in starting_slots:
                        boardObj.board[index//9][index%9] = 2

                if event.key == pygame.K_3:
                    index = find_square_clicked(click_pos, True)
                    if (index//9, index%9) not in starting_slots:
                        boardObj.board[index//9][index%9] = 3

                if event.key == pygame.K_4:
                    index = find_square_clicked(click_pos, True)
                    if (index//9, index%9) not in starting_slots:
                        boardObj.board[index//9][index%9] = 4

                if event.key == pygame.K_5:
                    index = find_square_clicked(click_pos, True)
                    if (index//9, index%9) not in starting_slots:
                        boardObj.board[index//9][index%9] = 5

                if event.key == pygame.K_6:
                    index = find_square_clicked(click_pos, True)
                    if (index//9, index%9) not in starting_slots:
                        boardObj.board[index//9][index%9] = 6

                if event.key == pygame.K_7:
                    index = find_square_clicked(click_pos, True)
                    if (index//9, index%9) not in starting_slots:
                        boardObj.board[index//9][index%9] = 7
                
                if event.key == pygame.K_8:
                    index = find_square_clicked(click_pos, True)
                    if (index//9, index%9) not in starting_slots:
                        boardObj.board[index//9][index%9] = 8

                if event.key == pygame.K_9:
                    index = find_square_clicked(click_pos, True)
                    if (index//9, index%9) not in starting_slots:
                        boardObj.board[index//9][index%9] = 9

        draw_window(None)


def find_square_clicked(position, typing):  # returns the index of the box, typing is true if the user is typing a num
    global square_clicked

    for x in range(len(boxes)):
            if boxes[x][0][0] <= position[0] <= boxes[x][0][1] and\
            boxes[x][1][0] <= position[1] <= boxes[x][1][1]:
                if square_clicked and z == x and not typing:
                    square_clicked = False
                else:
                    square_clicked = True
                return x
    return -1

main()
# print(pygame.font.get_fonts())


    # pygame.draw.rect(WINDOW, (155, 155, 155), (boxes_starting_corners[1][0]+1, boxes_starting_corners[1][1], 69+1, 69+1))
    # pygame.draw.rect(WINDOW, (155, 155, 155), (boxes_starting_corners[0][0], boxes_starting_corners[0][1], 69+1, 69+1))
    # pygame.draw.rect(WINDOW, (155, 155, 155), (boxes_starting_corners[2][0]+1, boxes_starting_corners[2][1], 69+1, 69+1))
    # pygame.draw.rect(WINDOW, (155, 155, 155), (boxes_starting_corners[3][0], boxes_starting_corners[3][1], 69+1, 69+1))
    # pygame.draw.rect(WINDOW, (155, 155, 155), (boxes_starting_corners[4][0]+1, boxes_starting_corners[4][1], 69+1, 69+1))
    # pygame.draw.rect(WINDOW, (155, 155, 155), (boxes_starting_corners[5][0]+1, boxes_starting_corners[5][1], 69+1, 69+1))
    # pygame.draw.rect(WINDOW, (155, 155, 155), (boxes_starting_corners[6][0], boxes_starting_corners[6][1], 69+1, 69+1))
    # pygame.draw.rect(WINDOW, (155, 155, 155), (boxes_starting_corners[7][0]+1, boxes_starting_corners[7][1], 69+1, 69+1))
    # pygame.draw.rect(WINDOW, (155, 155, 155), (boxes_starting_corners[8][0]+1, boxes_starting_corners[8][1], 69+1, 69+1))
    # pygame.draw.rect(WINDOW, (155, 155, 155), (boxes_starting_corners[8][0]+71, boxes_starting_corners[8][1], 69+2, 69+1))
    # pygame.draw.rect(WINDOW, (155, 155, 155), (boxes_starting_corners[8][0]+71+1, boxes_starting_corners[8][1]+71*2+1, 69+1, 69+1))
    # pygame.draw.line(WINDOW, GREEN, (25, border_width+6+69+1), (25, border_width+6+69*2), 5)
    # pygame.draw.rect(WINDOW, GREEN, (border_width+5+70+1, boxes_starting_corners[0][1], 69, 69))



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
    