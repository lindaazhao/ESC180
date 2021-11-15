def is_empty(board):
    '''Return True iff there are no stones on the board <board>'''
    board_height = len(board)
    board_width = len(board[0])

    for i in range(board_height):
        for j in range(board_width):
            if board[i][j] != " ":
                return False
    return True

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board

def is_bounded(board, y_end, x_end, length, d_y, d_x):
    '''Return whether a sequence of length <length> is 
    "OPEN", "SEMIOPEN", or "CLOSED"'''

    # Set y, x variables for first tile in sequence
    start_y = y_end - d_y*(length-1)
    start_x = x_end - d_x*(length-1)

    if start_y - d_y < 0 or start_x - d_x < 0: # Starts at edge in relevant direction
        start_seq = "E"
    else:
        start_seq = board[start_y - d_y][start_x - d_x]

    if y_end + d_y > len(board) - 1 or x_end + d_x > len(board[0]) - 1: # Edge
        end_seq = "E"
    else:
        end_seq = board[y_end + d_y][x_end + d_x]

    print("IS BOUNDED", start_seq, end_seq) # TEST, remove this after

    if start_seq == " " and end_seq == " ":
        return "OPEN"
    elif start_seq == " " or end_seq == " ":
        return "SEMIOPEN"
    else:
        return "CLOSED"

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

def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x

def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    '''Return a tuple whose first element is # of open sequences of <col>
    and <length> in the row R, and whose second element is the # of 
    semi-open sequences of <col> and <length>. 
    Assume y_start, x_start is at the edge of the board'''
    open_seq_count, semi_open_seq_count = 0, 0

    cur_seq_length = 0
    cur_y = y_start
    cur_x = x_start

    while cur_y < len(board) and cur_x < len(board[0]):
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

    return open_seq_count, semi_open_seq_count

def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def detect_rows(board, col, length):
    '''Return a tuple, whose first element is # of open sequences of <col> and
    <length>, and whose second element is # of semi-open
    sequences of <col> and <length> on the entire board.'''
    open_seq_count, semi_open_seq_count = 0, 0

    # Check diagonals: 1, 1 and 1, -1

    for y in range(len(board)): 
        # Check every row
        open_0_1, semi_open_0_1 = detect_row(board, col, y, 0, length, 0, 1)
        print("Row", y, open_0_1)

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

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 5, 2, 0, 1, 3, 'w')
    put_seq_on_board(board, 0, 3, 0, 1, 3, 'w')
    put_seq_on_board(board, 2, 2, 1, 1, 3, 'w')
    print_board(board)
    print("Detect Row", detect_row(board, col, 2, 2, 3, 1, 1))
    print(detect_rows(board, col, length))
    # if detect_rows(board, col,length) == (3,0):
    #     print("TEST CASE for detect_rows PASSED")
    # else:
    #     print("TEST CASE for detect_rows FAILED")

if __name__ == '__main__':
    test_detect_rows()

