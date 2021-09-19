from random import randint

class Board:
    def __init__(self) -> None:
        self.board = [  [0, 0, 0, 0, 0, 0, 0, 0 ,0], 
                        [0, 0, 0, 0, 0, 0, 0, 0 ,0], 
                        [0, 0, 0, 0, 0, 0, 0, 0 ,0],
                        [0, 0, 0, 0, 0, 0, 0, 0 ,0],
                        [0, 0, 0, 0, 0, 0, 0, 0 ,0], 
                        [0, 0, 0, 0, 0, 0, 0, 0 ,0],
                        [0, 0, 0, 0, 0, 0, 0, 0 ,0],
                        [0, 0, 0, 0, 0, 0, 0, 0 ,0],
                        [0, 0, 0, 0, 0, 0, 0, 0 ,0]  ]
        
        self.solved_board = []  # call a function to solve it
        self.size = len(self.board)


    def print_board(self):
        for i in range(self.size):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - ")
            
            for j in range(self.size):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")


    def set_board(self, difficulty):
        if difficulty == 1:
            numofslots = randint(36, 39)
        elif difficulty == 2:
            numofslots = randint(30, 32)
        else:
            numofslots = randint(23, 25)

        starting_slots_pos = []
        j = 0
        while j < numofslots:
            new_loc = (randint(0, 8), randint(0, 8))
            #check for dupes
            if new_loc not in starting_slots_pos:
                starting_slots_pos.append(new_loc)
                j += 1

        # step 2
        starting_num_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        i = 0
        while i < numofslots:
            pos = starting_slots_pos[i]
            num_in_pos = randint(1, 9)
            if starting_num_count[num_in_pos] < 6:
                self.board[pos[0]][pos[1]] = num_in_pos
                i += 1
                starting_num_count[num_in_pos] += 1
        return starting_slots_pos