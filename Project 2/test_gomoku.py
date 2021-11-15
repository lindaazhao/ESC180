def is_empty(board):
    '''Return True iff there are no stones on the board <board>'''
    board_height = len(board)
    board_width = len(board[0])

    for i in range(board_height):
        for j in range(board_width):
            if board[i][j] != " ":
                return False
    return True
    
    
def is_bounded(board, y_end, x_end, length, d_y, d_x):
    '''Return whether a sequence of length <length> is 
    "OPEN", "SEMIOPEN", or "CLOSED"'''

    # Set y, x variables for first tile in sequence
    start_y = y_end - d_y*(length-1)
    start_x = x_end - d_x*(length-1)

    if start_y - d_y < 0 or start_x - d_x < 0 or start_x - d_x >= len(board[0]): # Starts at edge in relevant direction
        start_seq = "E"
    else:
        start_seq = board[start_y - d_y][start_x - d_x]

    if y_end + d_y > len(board) - 1 or x_end + d_x > len(board[0]) - 1: # Edge
        end_seq = "E"
    else:
        end_seq = board[y_end + d_y][x_end + d_x]

    print("IS BOUNDED, Start:", start_seq, "End:", end_seq) # TEST, remove this after

    if start_seq == " " and end_seq == " ":
        return "OPEN"
    elif start_seq == " " or end_seq == " ":
        return "SEMIOPEN"
    else:
        return "CLOSED"

    
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    '''Return a tuple whose first element is # of open sequences of <col>
    and <length> in the row R, and whose second element is the # of 
    semi-open sequences of <col> and <length>. 
    Assume y_start, x_start is at the edge of the board'''
    open_seq_count, semi_open_seq_count = 0, 0

    cur_seq_length = 0
    cur_y = y_start
    cur_x = x_start

    while 0 <= cur_y < len(board) and 0 <= cur_x < len(board[0]):
        if board[cur_y][cur_x] == col: 
            cur_seq_length += 1 
            if cur_seq_length == length:
                y_end = cur_y # Set endpoints for is_bounded()
                x_end = cur_x

                # Determine how sequence is bound, increment respective counter
                if is_bounded(board, y_end, x_end, length, d_y, d_x) == "OPEN":
                    open_seq_count += 1
                elif is_bounded(board, y_end, x_end, length, d_y, d_x) == "SEMIOPEN":
                    semi_open_seq_count += 1
        else: # If current coord != colour
            cur_seq_length = 0
        cur_y += d_y # Check next coordinate in direction next loop
        cur_x += d_x

    return open_seq_count, semi_open_seq_count


def detect_rows(board, col, length):
    '''Return a tuple, whose first element is # of open sequences of <col> and
    <length>, and whose second element is # of semi-open
    sequences of <col> and <length> on the entire board.'''
    open_seq_count, semi_open_seq_count = 0, 0

    for y in range(len(board)): 
        # Check every row
        open_0_1, semi_open_0_1 = detect_row(board, col, y, 0, length, 0, 1)
        # Check lower left half of 1,1 diagonals
        open_1_1, semi_open_1_1 = detect_row(board, col, y, 0, length, 1, 1)
        # Check lower right half of 1,-1 diagonals
        open_1_neg1, semi_open_1_neg1 = detect_row(board, col, y, len(board[0])-1, length, 1, -1)

        open_seq_count += open_0_1 + open_1_1 + open_1_neg1
        semi_open_seq_count += semi_open_0_1 + semi_open_1_1 + semi_open_1_neg1

    for x in range(len(board[0])): 
        # Check every column 
        open_1_0, semi_open_1_0 = detect_row(board, col, 0, x, length, 1, 0)
        # Check upper right half of 1,1 diagonals
        if x > 0:
            open_1_1, semi_open_1_1 = detect_row(board, col, 0, x, length, 1, 1)
        # Check upper left half of 1,-1 diagonals
        if x < len(board[0]) - 1:
            open_1_neg1, semi_open_1_neg1 = detect_row(board, col, 0, x, length, 1, -1)
    
        open_seq_count += open_1_0 + open_1_1 + open_1_neg1
        semi_open_seq_count += semi_open_1_0 + semi_open_1_1 + semi_open_1_neg1

    return open_seq_count, semi_open_seq_count
    

def search_max(board):
    '''Return a tuple (y, x) such that putting a black stone in 
    coordinates (y, x) maximizes the potential score'''
    max_score = score(board)
    move_y, move_x = 0, 0

    for y in range(len(board)): 
        for x in range(len(board[0])):
            if board[y][x] == " ": # Square is empty
                board[y][x] = "b"
                if score(board) > max_score:
                    max_score = score(board) # New max_score to beat
                    move_y = y
                    move_x = x
                board[y][x] = " " # Reset board after score and move are saved

    return move_y, move_x

def score(board):
    '''Calculate overall score (b & w) for the board'''
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

# Given Functions
def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    
def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board

def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x

# Test Cases for Specific Functions
def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")

def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

if __name__ == '__main__':
    test_search_max()

