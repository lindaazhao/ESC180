##PROBLEM 2: Sum of Cubes

#method 1: loop 1^3 ... + n^3
#method 2: (1 + ... + n )^2
sum1 = 0
sum2 = 0
sum3 = 0

n = 3
N = 8

def method1(n):
    for i in range(1, n+1):
        sum1 += i**3
def method2(n)
    for i in range(1, n+1):
        sum2 += (i)
    sum2 = sum2**2

print(method1(n))
print(method2(n))


def check_sum(n):
    #check that 2 methods of calculating match
    # if yes, return true, if not, return false

    if sum2 == sum1:
        return True
    else:
        return False

def check_sums_up_to_n(N):
    #check that formula 2 works for every n≤N
    #returns True iff for every n≤N, if no return false
    if n <= N:
        sum3 = 0
        for i in range(1, n+1):
            sum3 += i

        sum3 = sum3 **2

        if (sum3) == sum2:
            return True

        else:
            return False


print(check_sum(n))
print(check_sums_up_to_n(N))



##PROBLEM 3: PI
#use for, while loops to compute = ((-1)**n))/(2n+1) --> sum of values of n = 0 , 100
#print approximation of value of pi (result of sum formula = pi/4)

sum = 0
for i in range(0,1001):
    res = ((-1)**i)/(2*i + 1)
    sum += res

print(sum*4)
