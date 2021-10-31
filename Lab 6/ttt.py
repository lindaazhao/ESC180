'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random
# Minimax optimization
# Breadth first / depth first

# ==================================================
# Problem 1 (a)
def move_coord(square_num):
    '''square_num is an integer between 1 and 9'''
    coord = [(square_num - 1) // 3, (square_num -1) % 3]
    return coord


# Problem 1 (b)
def put_in_board(board, mark, square_num):
    coord = move_coord(square_num)
    board[coord[0]][coord[1]] = mark


# ==================================================
# Problem 2 (a)
def get_free_squares(board):
    '''Return a list containing the coordinates of the free squares in the board.'''
    free_squares = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                free_square = [i, j]
                free_squares.append(free_square)
    return free_squares


# Problem 2 (b)
def make_random_move(board, mark):
    '''Find a random free square in board and put mark in that square.'''
    free_squares = get_free_squares(board)
    num_free_squares = len(free_squares)
    random__index = int(num_free_squares * random.random())
    coord = free_squares[random__index]
    board[coord[0]][coord[1]] = mark


# ==================================================
# Problem 3 (a)
def is_row_all_marks(board, row_i, mark):
    return board[row_i][0] == board[row_i][1] == board[row_i][2] == mark


# Problem 3 (b)
def is_col_all_marks(board, col_i, mark):
    return board[0][col_i] == board[1][col_i] == board[2][col_i] == mark


# Problem 3 (c)
def is_win(board, mark):
    for i in range(3):
        if is_row_all_marks(board, i, mark) or \
            is_col_all_marks(board, i, mark): 
                return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == mark or \
        board[0][2] == board[1][1] == board [2][0] == mark:
            return True
    return False


# ==================================================
# Problem 4 (a)
def put_in_board_w_coord(board, mark, coord):
    board[coord[0]][coord[1]] = mark


def make_winning_move(board, mark):
    free_squares = get_free_squares(board)
    for i in range(len(free_squares)):
        square_num = free_squares[i]
        # print(square_num)
        put_in_board_w_coord(board, mark, square_num)
        if is_win(board, mark):
            return square_num
        else:
            put_in_board_w_coord(board, " ", square_num)
    return None


# Problem 4 (b)
def block_opponent_win(board, mark):
    X_winning_move = make_winning_move(board, "X")

    if X_winning_move is not None:
        put_in_board_w_coord(board, mark, X_winning_move)
        return X_winning_move
    else:
        return None


# ==================================================
# Starter functions
def print_board_and_legend(board):
    for i in range(3):
        # First board
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        # Second board with reference #s
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        # Print first and second board row with 5 spaces separating the boards
        print(line1 + " "*5 + line2)
        # Print line separators
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")

def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board
    
# ==================================================
# ==================================================      
if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)

    # Problem 1 (c) - Human player vs human player game
    # move_count = 0
    # while move_count < 9:
    #     if move_count % 2 == 0:
    #         input_coord = int(input("Please enter a coordinate for X: "))
    #         put_in_board(board, "X", input_coord)
    #     else:
    #         input_coord = int(input("Please enter a coordinate for O: "))
    #         put_in_board(board, "O", input_coord)
    #     print(get_free_squares(board))
    #     move_count += 1
    #     print("\n")
    #     print_board_and_legend(board) 

    # Human player vs computer game
    # Assume human player always starts ==> always uses "X"
    move_count = 0
    while move_count < 9:
        if move_count % 2 == 0:
            input_coord = int(input("Please enter a coordinate for X: "))
            put_in_board(board, "X", input_coord)
        else:
            # Problem 4 (a) Implementation
            O_winning_move = make_winning_move(board, "O")
            if O_winning_move is None:
                # Problem 4 (b) Implementation
                O_blocking_move = block_opponent_win(board, "O")
                if O_blocking_move is None:
                    # Problem 2 (c)
                    make_random_move(board, "O")

        # Problem 3 (d)
        if is_win(board, "X") == True:
            print("\n")
            print_board_and_legend(board)
            print("Game over! X won.")
            break
        elif is_win(board, "O") == True:
            print("\n")
            print_board_and_legend(board)
            print("Game over! O won.")
            break

        # print(get_free_squares(board))
        move_count += 1
        print("\n")
        print_board_and_legend(board)
            