import numpy as np

#
# # Printing matrices using NumPy:
#
# # Convert a list of lists into an array:
# M_listoflists = [[1,-2,3],[3,10,1],[1,5,3]]
# M = np.array(M_listoflists)
# # Now print it:
# print(M)
#
#
#
#
# #Compute M*x for matrix M and vector x by using
# #dot. To do that, we need to obtain arrays
# #M and x
# M = np.array([[1,-2,3],[3,10,1],[1,5,3]])
# x = np.array([75,10,-11])
# b = np.matmul(M,x)
#
# print(M)
# #[[ 1 -2  3]
# # [ 3 10  1]
# # [ 1  5  3]]
#
# # To obtain a list of lists from the array M, we use .tolist()
# M_listoflists = M.tolist()
#
# print(M_listoflists) #[[1, -2, 3], [3, 10, 1], [1, 5, 3]]

##
def print_matrix(M_lol):
    print(np.array(M_lol))

##
def get_lead_ind(row):
    no_nonzeros = True
    for i in range(len(row)):
        if row[i] != 0:
            return i
            no_nonzeros = False

    if no_nonzeros == True:
        return len(row)

##
def get_row_to_swap(M, start_i):
    leading_non_zero_coeff_i = []
    for i in range(start_i,len(M)): #iterate through rows
        leading_non_zero_coeff_i.append(get_lead_ind(M[i]))
        index = leading_non_zero_coeff_i.index(min(leading_non_zero_coeff_i))
    return (index + start_i)

##
def add_rows_coefs(r1, c1, r2, c2):
    new_list = []
    for i in range(len(r1)):
        value = c1*r1[i] + c2*r2[i]
        new_list.append(value)

    return new_list
##
def eliminate(M, row_to_sub, best_lead_ind):
    for i in range(row_to_sub + 1, len(M)):
        r1 = M[row_to_sub]
        r2 = M[i]
        c1 = -1 * M[i][best_lead_ind]
        c2 = 1 * M[row_to_sub][best_lead_ind]
        M[i] = add_rows_coefs(r1,c1,r2,c2)

    return M

##
def forward_step(M):
    best_M = M[:]

    for i in range(len(M)-1): #row num = i
        lead_ind = get_lead_ind(M[i])
        if lead_ind != i:
            row_num_swap = get_row_to_swap(M,i)
            best_M[i] = M[row_num_swap]
            best_M[row_num_swap] = M[i]
            best_M = eliminate(best_M,i, get_lead_ind(best_M[i]))
            M = best_M

    print_matrix(best_M)



M = [[5, 6, 7, 8],
[0,0, 1, 1],
[0, 0, 5, 2],
[0, 0, 7, 0]]

forward_step(M)

##
# def backward_step(M):


##
# def build_aug_M(M,x):
#     b = np.matmul(M,x)