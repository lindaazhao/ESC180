#prob 1
# True iff list1 is at least as long as list2, and the first len(list2) elements of list1 are the same as list2.
# Note: len(lis) is the length of the list lis i.e., the number of elements in lis. First write the function without using slicing ("slicing" means doing things like list1[2:5]), and using a loop.

def list1_starts_with_list2(list1, list2):
    if len(list1) <= len(list2):
        return True
    else:
        return False


print(list1_starts_with_list2([1,2,3,4,],[1,2,3,4,5]))

#prob 2
#True if same order
#special test case, if L2 larger than L1 and you check up to L1

def match_pattern(list1, list2):
    if len(list1) == len(list2):
        for i in range(len(list1)):
            if list1[i] == list2[i]:
                return True
            else:
                return False

    if len(list1) >= len(list2):
        for i in range(len(list2)):
            if list1[i] == list2[i]:
                return True, "Matched up to end of list2"
            else:
                return False

    if len(list1) <= len(list2):
        for i in range(len(list1)):
            if list1[i] == list2[i]:
                return True, "Matched up to end of list1"
            else:
                return False

print(match_pattern([1,2,3,4],[1,2,3]))

#prob 3
#def repeats(list0), which returns True iff list0 contains at least two adjacent elements with the same value

def repeats(list0):
    for i in range(len(list0)):
        if list0[i] == list0[i+1]:
            return True
        else:
            return False

print(repeats([1,2,3,4,5]))

#prob 4
#4a
def print_matrix_dim(M): #return numrow x numcolumns
    num_rows = len(M)
    num_columns = len(M[1])

    print(num_rows,num_columns,sep="x")
M = [1,2],[3,4],[5,6]

print_matrix_dim(M)

#4b
# ten_zeros1 = [0]*10
#
# ten_zeros2 = []
# for i in range(10):
#   ten_zeros2.append(0)
prod_storage = []
sum_storage = []

def mult_M_v(M, v):
    if len(v) == len(M[1]):
        for i in range(len(M)):
            prod_storage = []
            for j in range(len(M[1])):
                prod = M[i][j]*v[i]
                prod_storage.append(prod)
            get_sum(prod_storage)
        return sum_storage

def get_sum(L):
    sum = 0
    for k in range(len(L)):
        sum += L[k]
    sum_storage.append(sum)

v1 = [1,
    2,
    3]

M1 = [[4,5,6],
    [7,8,9],
    [10,11,12]]

print(mult_M_v(M1, v1))



