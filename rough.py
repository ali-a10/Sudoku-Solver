# from random import randint
from Board import *

boardObj = Board()

# 1. (assuming difficulty is easy)  generate 36-39 random tuples (positions)
##### make sure there are no duplicate positions

# 2. loop through the positions, and for each position, generate a random number
##### b/w 1-9, but make sure no number is put on the board more than 6 times or 0 times
##### maybe use a list of lists of pairs, where the first element is the number and the
##### second is the amount of times it's currently shown on the board. Also, on the 
##### last position pair, check if there's a number that hasn't been placed on the board and use it

            
difficulty = int(input("select difficulty, 1(easy) 2(medium), 3(hard): "))

if difficulty == 1:
    # step 1
    numofslots = randint(36, 39)
    print(numofslots)
    boardObj.set_board(numofslots)  # could remove numofslots variable

elif difficulty == 2:
    numofslots = randint(2, 8)  # change
    print(numofslots)
    boardObj.set_board(numofslots)  # could remove numofslots variable

elif difficulty == 3:
    numofslots = randint(36, 39)  # change
    print(numofslots)
    boardObj.set_board(numofslots)  # could remove numofslots variable


else:
    difficulty = int(input("input valid number: 1(easy) 2(medium), 3(hard): "))

        
boardObj.print_board()
# count = 0
# starting_num_count2 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
# for i in range(9):
#     for j in range(9):
#         if board[i][j] != 0:
#             count += 1
#             starting_num_count2[board[i][j]] += 1

# print(count)
# print(starting_num_count2)