# Problem 1
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)


# Problem 2
def interleave(L1, L2):
    if len(L1) == len(L2) == 1:
        return L1 + L2
    else:
        lastL1 = [L1[-1]]
        lastL2 = [L2[-1]]
        del L1[-1]
        del L2[-1]
        return interleave(L1, L2) + interleave(lastL1, lastL2)

print(interleave([1, 3, 5, 7], [2, 4, 6, 8]))


# Problem 3
def reverse_rec(L):
    if len(L) == 1:
        return L
    else:
        if L[1:len(L)-1] == []:
            return [L[len(L)-1]] + [L[0]] # Work for even length lists too
        else:
            return [L[len(L)-1]] + reverse_rec(L[1:len(L)-1]) + [L[0]]

print(reverse_rec([1, 2, 3, 4, 5, 6, 7]))

# Problem 4
def zigzag(L):
    if len(L) == 0:
        return L
    elif len(L) % 2 == 0:
        return [L.pop(len(L) // 2 - 1)] + zigzag(L)
    else:
        return [L.pop(len(L) // 2)] + zigzag(L)

print(zigzag([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# Problem 5
