import math

## Problem 1: Count Evens in a List
def count_evens(L):
    '''Returns # of even integers in list L'''
    counter = 0
    for i in L:
        if i % 2 == 0:
            counter += 1
    return counter

print("Count Evens Test 1:", count_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print("Count Evens Test 2:", count_evens([2, 4, 6, 8, 10]))

## ==================================================
## Problem 2: List to String
def list_to_str(lis):
    '''Returns the string representation of the list'''
    string = "["
    for i in lis:
        string += str(i) + ", "
    string = string[:-2] # Removes the ", " after the last index of the list is added
    string += "]"
    return string
    # There's probably a more efficient way to do this

print("List to String Test:", list_to_str([1, 2, 3, 4, 5]))

## ==================================================
## Problem 3: Comparing Lists
def lists_are_the_same(list1, list2):
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True

print("Same Lists Test 1:", lists_are_the_same([4, 5, 6], [1, 2, 3]))
print("Same Lists Test 2:", lists_are_the_same([1, 2, 3], [1, 2, 3]))

## ==================================================
## Problem 4: Simplifying Fractions
def simplify_fraction(n, m):
    '''Prints the simplified version of n/m, returns greatest common divisor'''
    max_divisor = max(n, m)
    # print(max_divisor)
    if not n == 0 or m == 0:
        for i in range(max_divisor+1):
            # print("Test1:", n % (max_divisor-i))
            # print("Test2:", m % (max_divisor-i))
            if n % (max_divisor-i) == 0 and m % (max_divisor-i) == 0:
                print(n//i, "/", m//i, sep="")
                return i
    return None

simplify_fraction(8, 4)
simplify_fraction(0, 1)

## ==================================================
## Problem 5: Sum more pi
def approx_pi(n):
    '''Returns # of terms required for approximation of pi to match pi to n S.D.s'''    
    int_pi_to_n = int(math.pi*(10**n)) # Real pi to n sig figs that we need to check against
    quarter_pi = 0
    num_terms = 0

    while int((quarter_pi*4)*10**n) != int_pi_to_n:
        res = ((-1)**num_terms)/(2*num_terms + 1)
        quarter_pi += res
        num_terms += 1

    print(quarter_pi*4)
    return num_terms

print(approx_pi(3))
print(approx_pi(6))