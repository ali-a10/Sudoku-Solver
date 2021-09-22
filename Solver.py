
from typing import runtime_checkable


def valid_move(board, number, position):
    # check column
    for row in range(len(board)):
        if board[row][position[1]] == number and position[0] != row:
            return False
        
    # check row
    for col in range(len(board)):
        if board[position[0]][col] == number and position[1] != col:
            return False

    # check box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if board[i][j] == number and (i, j) != position:
                return False