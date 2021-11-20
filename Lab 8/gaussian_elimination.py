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
        row_sum[i] = r1[i]*c1 + r2[i]*c2

    return row_sum


# Problem 5
def eliminate(M, row_to_sub, best_lead_ind):
    '''Return M where all the rows below <row_to_sub> have the 
    values at index <best_lead_ind> eliminated. 
    Assume best_lead_ind is get_lead_ind(M[row_to_sub])'''
    for i in range(1, len(M)-row_to_sub): # Number of rows below row_to_sub
        while M[row_to_sub+i][best_lead_ind] != 0: # Number in column <best_lead_ind>
            for j in range(len(M[row_to_sub])):
                M[row_to_sub+i][j] -= M[row_to_sub][j] # Subtract elements of <row_to_sub> from elements of row

    return M


# Problem 6
def forward_step(M):
    pass


# Problem 7
def backward_step(M):
    pass


# Problem 8
def solve(M, b):
    pass


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
    print(get_row_to_swap(M1, start_i))

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



