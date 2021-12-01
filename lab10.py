##1
def power(x,n):
    #print(x, "^" ,n)
    res = 1
    if n == 0:
        res = 1
    else:
        for i in range (1,n+1):
            res = res * x
    return res


##2
def interleave_loop(L1,L2):
    combinedL = []
    for i in range(len(L1)):
        combinedL.append(L1[i])
        combinedL.append(L2[i])
    return combinedL


import operator
from functools import reduce

def interleave(L1, L2):
    return reduce(operator.add, zip(L1, L2))


##3
def reverse_rec(L):
    L1 = L[::-1]
    L.reverse()
    return L1,L


##4

if __name__ == "__main__":
    print(power(8,0))

    print(interleave([1,3,5,7],[2,4,6,8]))

    print(reverse_rec([1,2,3,4]))
