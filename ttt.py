'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random


# Problem 1 (a)
def move_coord(square_num):
    '''square_num is an integer between 1 and 9'''
    coord = [(square_num - 1) // 3, (square_num -1) % 3]
    return coord


# Problem 1 (b)
def put_in_board(board, mark, square_num):
    coord = move_coord(square_num)
    board[coord[0]][coord[1]] = mark

# Problem 2 (a)
def get_free_squares(board):
    free_squares = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                free_square = [i, j]
                free_squares.append(free_square)
    return free_squares


# Problem 2 (b)
def make_random_move(board, mark):
    num_free_squares = len(get_free_squares(board)) # Fix this
    print(num_free_squares)
    free_squares = get_free_squares(board)
    print(free_squares)
    coord = free_squares[int((num_free_squares + 1) * random.random())] # Fix this
    board[coord[0]][coord[1]] = mark

def is_row_all_marks(board, row_i, mark):
    return board[row_i][0] == board[row_i][1] == board[row_i][2] == mark

def is_col_all_marks(board, col_i, mark):
    return board[0][col_i] == board[1][col_i] == board[2][col_i] == mark

def is_win(board, mark):
    for i in range(3):
        if is_row_all_marks(board, i, mark) == True or \
            is_col_all_marks(board, i, mark) == True: 
                return True
    if board[0][0] == board[1][1] == board[2][2] == mark or \
        board[0][2] == board[1][1] == board [2][0] == mark:
            return True
    return False


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

def make_winning_move(board, mark):
    free_squares = get_free_squares(board)
    for i in range(len(free_squares)):
        square_num = free_squares[i]
        print(square_num)
        put_in_board(board, mark, square_num[0] * 3 + square_num[1] + 1)
        if is_win(board, mark) == True:
            print("Made a winning move 😎")
            return True
        else:
            board[square_num[0]][square_num[1]] = " "

    return False

    #check if X is about to win 
    

    
if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)

    # Problem 1 (c)
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

    # Problem 2 (c)
    move_count = 0
    while move_count < 9:
        if move_count % 2 == 0:
            input_coord = int(input("Please enter a coordinate for X: "))
            put_in_board(board, "X", input_coord)
        else:
            make_winning_move(board, "O")
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

        print(get_free_squares(board))
        move_count += 1
        print("\n")
        print_board_and_legend(board)
            