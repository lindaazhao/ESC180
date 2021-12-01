## PROBLEM 2: Sum of Cubes

def sum_of_cubes1(n):
    '''Compute 1^3 + 2^3 + ... + n^3'''
    # **Removed "global"s, don't need them here (and try not to use them in general)
    cubesum = 0
    for i in range(1, n+1):
        cubesum += i**3
    return cubesum


def sum_of_cubes2(n):
    '''Compute 1^3 + 2^3 + ... + n^3 using formula 
    1^3 + 2^3 + ... + n^3 = (1 + 2 + ... + n)^2'''
    rawsum, cubesum = 0, 0
    for i in range(1, n+1):
        rawsum += (i)
    cubesum = rawsum**2
    return cubesum


# Check to make sure both functions work
print(sum_of_cubes1(3))
print(sum_of_cubes2(3))


# Function check to make sure both above functions work
def check_sum(n):
    '''Checks if the results of sum_of_cubes1 and sum_of_cubes2 match, 
    returns True/False'''

    # **Can just return the boolean instead of using if/else
    return sum_of_cubes1(n) == sum_of_cubes2(n)

    # if sum_of_cubes1(n) == sum_of_cubes2(n):
    #     return True
    # else:
    #     return False


def check_sums_up_to_n(N):
    '''Checks that sum_of_cubes2 works (equals sum_of_cubes1) for every n≤N, 
    returns True/False '''

    n = 0
    while n <= N:
        if not(sum_of_cubes1(n) == sum_of_cubes2(n)):
            print("Found one that doesn't work!: ", n)
            return False
        else:
            print("Just checked ", n)
            n += 1
        
    return True

# Checks that the above function is doing its job
print(check_sums_up_to_n(50))

## ==================================================
## PROBLEM 3: PI
# Use for/while loops to compute sum of values ((-1)**n))/(2n+1) for n = 0 to n = 1000
# Print approximation of value of pi (result of sum formula = pi/4)

# Using a for loop
sum = 0
for n in range(1001):
    res = ((-1)**n)/(2*n + 1)
    sum += res

print(sum*4)

# Using a while loop
def compute_pi(last_index):
    pi_sum, n = 0, 0

    while n <= last_index:
        pi_sum += ((-1)**n)/(2*n + 1)
        n += 1

    return pi_sum*4

print(compute_pi(1000))
print(compute_pi(1000000))