# Problem 1 ==================================================
def list1_starts_with_list2(list1, list2):
    '''Return True iff list1 is at least as long as list2, and the first 
    len(list2) elements of list1 are the same as list2'''
    if len(list1) >= len(list2): # First condition
        for i in range(len(list2)):
            if not list2[i] == list1[i]: # Second condition
                return False
        return True # At the end to ensure all of list2 is in list1
    return False

print("========== Problem 1 Tests ==========")
print(list1_starts_with_list2([1, 2, 3, 4, 5], [1, 2, 3]))
print(list1_starts_with_list2([1, 2, 3, 4, 5], [1, 3, 5]))
print(list1_starts_with_list2([1, 2, 3, 4, 5], [2, 3, 4]))
print(list1_starts_with_list2([1, 2, 3], [1, 2, 3, 4, 5]))


# Problem 2 ==================================================
def match_pattern(list1, list2):
    '''Returns true iff the pattern list2 appears in list1'''
    list1_index = 0
    list_match = False

    if len(list1) >= len(list2):
        for i in range(len(list1)):
            if list1_starts_with_list2(list1[i:], list2):
                return True

    # return list_match
    return False
    
print("========== Problem 2 Tests ==========")
print(match_pattern([4, 10, 2, 3, 50, 100], [2, 3, 50]))
print(match_pattern([4, 10, 2, 2, 3, 50, 100], [2, 3, 50]))
print(match_pattern([4, 10, 2, 3, 50, 100], [2, 4, 50]))
        
                
# Problem 3 ==================================================
def repeats(list0):
    '''Returns true iff list0 contains at least two adjacent elements 
    with the same value'''
    for i in range(len(list0)-1):
            if list0[i] == list0[i+1]: # Check next element in list
                return True
    return False

print("========== Problem 3 Tests ==========")
print(repeats([1, 2, 2, 3, 4]))
print(repeats([1, 2, 3, 4, 5]))

# Problem 4 ==================================================
# Problem 4(a)
def print_matrix_dim(M):
    '''Assume M is actually a matrix, rectangular'''
    print(len(M), len(M[0]), sep = "x")

print("========== Problem 4(a) Tests ==========")
print_matrix_dim([[1,2],[3,4],[5,6]])
print_matrix_dim([[5, 6, 7], [0, -3, 5]])

# Problem 4(b)
def mult_M_v(M, v):
    '''Assume v is (m, 1) in size'''

    Mv = []
    for i in range(len(M)):
        res = 0
        for j in range(len(M[i])):
            res += M[i][j] * v[j]
        Mv.append(res)
    return Mv

M1 = [[1, 2], 
      [3, 4], 
      [5, 6]]

v1 = [7, 8] 

M2 = [[1, 2],
      [3, 4]]

v2 = [5, 6]

print("========== Problem 4(b) Tests ==========")
print(mult_M_v(M1, v1))
print(mult_M_v(M2, v2))

# Problem 4(c)