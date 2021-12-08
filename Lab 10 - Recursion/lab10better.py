##1

def power(x,n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)



##2
def interleave(L1,L2):
    if len(L1) == 1 or len(L2) == 1: #last round, add both to back of new list
        L.append(L1[0])
        L.append(L2[0])
        return L


    else:
        L.append(L1[0])
        L.append(L2[0])

        L1 = L1[1:len(L1)]
        L2 = L2[1:len(L2)]


        return interleave(L1,L2)

##3
def reverse_rec(L1,L2):

    if len(L1) == 1: #last one return whole thing
        L2.append(L1[0])
        return L2

    else:
        L2.append(L1[-1])
        L1 = L1[0:len(L1)-1]

        return reverse_rec(L1,L2)




##4
def middle_side_rec(L1):
    L_left = L1[0:(len(L1)//2)]
    print(L_left)
    L_right = L1[len(L1)//2 + 1:len(L1)]
    print(L_right)

    L_left = reverse_rec(L_left,[])
    print(L_left)


    new_list = [L1[len(L1)//2]] + interleave(L_left,L_right)

    return new_list

##5
def is_balanced(s):
    left_bracket_count = 0
    right_bracket_count = 0

    slist = list(s)
    for i in range(len(slist)):
        if "(" == slist[i]:
            left_bracket_count += 1
        if ")" == slist[i]:
            right_bracket_count += 1
    if right_bracket_count == left_bracket_count:
        return ("True")
    else:
        return("False")


if __name__ == "__main__":
    # print(power(2,3))

    # L = []
    # print(interleave([1,3,5,7],[2,4,6,8]))

    # L1 = [1,2,3,4]
    # L2 = []
    # print(reverse_rec(L1,L2))

    L = []
    print(middle_side_rec([4,2,1,3,5]))

    print(is_balanced("(()(())"))




