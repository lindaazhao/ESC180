import numpy as np

# Problem 1
def print_matrix(M_lol):
    '''Print the nested list M_lol as a matrix (array)'''
    print(np.array(M_lol))


# Problem 2
def get_lead_ind(row):
    '''Return the index of the first non-zero element of <row>'''
    for i in range(len(row)):
        if row[i] != 0:
            return i
    return len(row) # If row does not contain non-zero elements


# Problem 3
def get_row_to_swap(M, start_i):
    '''Return the row that needs to be swapped with the row M[start_i]'''
    row1_lead = get_lead_ind(M[start_i]) # First non-zero index of given row
    lowest_lead = row1_lead # Lowest non-zero index of rows below
    row_to_swap = start_i
    
    for i in range(1, len(M)-start_i):
        current_lead = get_lead_ind(M[start_i+i])
        if current_lead < lowest_lead:
            lowest_lead = current_lead
            row_to_swap = start_i + i

    return row_to_swap


# Problem 4
def add_rows_coefs(r1, c1, r2, c2):
    '''Return a new list containing the row c1*r1 + c2*r2. Rows are lists of equal lengths'''
    row_sum = [0] * len(r1)

    for i in range(len(r1)):
        if r2[i]*c2 == int(r2[i]*c2):
            row_sum[i] = r1[i]*c1 + int(r2[i]*c2)
        else:
            row_sum[i] = r1[i]*c1 + r2[i]*c2
    return row_sum


# Problem 5
def eliminate(M, row_to_sub, best_lead_ind): # Forward step
    '''Return M where all the rows below <row_to_sub> have the 
    values at index <best_lead_ind> eliminated. 
    Assume best_lead_ind is get_lead_ind(M[row_to_sub])'''
    rts_lead = M[row_to_sub][best_lead_ind] # Magnitude of lead coef of row_to_sub
    rts = M[row_to_sub] # Actual row, row_to_sub

    for i in range(1, len(M)-row_to_sub): # Number of rows below row_to_sub
        while M[row_to_sub+i][best_lead_ind] != 0: # Number in column <best_lead_ind>
            row_at_bli = M[row_to_sub+i][best_lead_ind]
            M[row_to_sub+i] = add_rows_coefs(M[row_to_sub+i], 1, rts, -1*row_at_bli/rts_lead)
    return M


# Problem 6
def forward_step(M):
    for i in range(len(M)):
        swap_index = get_row_to_swap(M, i)
        M[swap_index], M[i] = M[i], M[swap_index]
        eliminate(M, i, get_lead_ind(M[i]))
    return M


# Problem 7
def backward_step(M):
    for i in range(len(M)-1, 0, -1):
        eliminate_back(M, i, get_lead_ind(M[i]))
    return M


def eliminate_back(M, row_to_sub, best_lead_ind): # Backward step, reverse ranges
    '''Return M where all the rows above <row_to_sub> have the 
    values at index <best_lead_ind> eliminated. 
    Assume best_lead_ind is get_lead_ind(M[row_to_sub])'''
    rts_lead = M[row_to_sub][best_lead_ind] # Magnitude of lead coef of row_to_sub
    rts = M[row_to_sub] # Actual row, row_to_sub

    for i in range(row_to_sub-1, -1, -1): # Count up rows from row_to_sub
        while M[i][best_lead_ind] != 0: # Number in column <best_lead_ind>
            row_at_bli = M[i][best_lead_ind]
            M[i] = add_rows_coefs(M[i], 1, rts, -1*row_at_bli/rts_lead)
    return M

def divide_by_leading_coef(M):
    for i in range(len(M)):
        leading_coef = M[i][get_lead_ind(M[i])]
        for j in range(len(M[i])):
            if M[i][j] / leading_coef == int(M[i][j] / leading_coef):
                M[i][j] = int(M[i][j] / leading_coef)
            else:
                M[i][j] /= leading_coef
    return M


# Problem 8
def solve(M, b):
    m = len(M) # of rows in M
    n = len(M[0]) # of columns in M

    for i in range(len(b)): # Turn into augmented matrix
        M[i].append(b[i])

    # Turn into reduced normal form [R|d]
    forward_step(M)
    backward_step(M)
    divide_by_leading_coef(M)
    
    rank = 0
    for i in range(len(M)):
        if get_lead_ind(M[i]) < len(M[i]):
            rank += 1
            print(rank)

    # Reduced vector b
    d = [0] * len(b)
    for i in range(len(M)):
        d[i] = M[i][-1]

    # Solution vector
    x = [0] * n

    if rank < m and rank < n: # Not full rank
        for i in range(1, m-rank+1):
            if d[-i] != 0:
                return "No solutions" 
        return "Infinite Solutions"

    elif m == n: # Square Matrix, m == n == rank
        for i in range(len(x)): # Find solution for x
            x[i] = d[i]
    elif m > n: # Tall & Thin Matrix, n == rank
        for i in range(1, m-rank+1):
            if d[-i] != 0:
                return "No solutions"
        for i in range(len(x)): # Find solution for x
            x[i] = d[i]
    elif n > m: # Short and Wide Matrix, m == rank
        return "Infinite solutions"
    
    return x
    

# Tests ==================================================
if __name__ == '__main__':
    # Problem 1
    print_matrix([[1,-2,3],[3,10,1],[1,5,3]])

    # Problem 3
    M1 = [[5, 6, 7, 8],
        [0, 0, 0, 1],
        [0, 0, 5, 2],
        [0, 1, 0, 0]]
    start_i = 1
    swap = get_row_to_swap(M1, start_i)
    print(swap)
    M1[swap], M1[start_i] = M1[start_i], M1[swap]
    print(M1)

    # Problem 4
    r1 = [1, 2, 3, 4]
    r2 = [1, 1, 1, 1]
    print(add_rows_coefs(r1, 2, r2, 2))

    # Problem 5
    M3 = [[5, 6, 7, 8],
        [0,0, 1, 1],
        [0, 0, 5, 2],
        [0, 0, 7, 0]]
    row_to_sub = 1
    best_lead_ind = 2
    print(eliminate(M3, row_to_sub, best_lead_ind))

    # Problem 6
    M4 = [[0, 0, 1, 0, 2], [1, 0, 2, 3, 4], [3, 0, 4, 2, 1], [1, 0, 1, 1, 2]]
    print(forward_step(M4))

    # Problem 7
    M5 = [[1, -2, 3, 22], [ 3, 10, 1, 314], [ 1, 5, 3, 92]]
    print(forward_step(M5))
    print(backward_step(M5))
    print(divide_by_leading_coef(M5))
    # print(solve(M5, [2, 3, 4]))

    M6 = [[0, 2], [3, -2]]
    b = [4, 5]
    print(solve(M6, b))







