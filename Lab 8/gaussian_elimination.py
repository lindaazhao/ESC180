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
    print("row1_lead:", row1_lead)
    lowest_lead = row1_lead # Lowest non-zero index of rows below
    print("lowest_lead:",lowest_lead)
    row_to_swap = start_i
    print("row_to_swap:", row_to_swap)
    
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
    pass


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

