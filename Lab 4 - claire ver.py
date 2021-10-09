##Lab 4: Loops and PI

##Prob 1 - DONE

def sum_nums(L):
  s = 0
  for num in L:
    s += num

  return s

def count_evens(L):
    count = 0
    for i in range(0, len(L)):
        if (L[i] % 2 == 0):
            count += 1
    return count

print(count_evens([1,2,3,4,5,6,7,8]))


##Prob 2 - DONE
#lis = L

def list_to_str(lis):
    #SHOULD DO: return(str(lis))
    if len(lis) == 0:
        return "'[]'"
    else:
        print("[", end="")
        for i in range(0, len(lis)-1):
            print(lis[i], " ", sep=",", end='')
        print(lis[len(lis)-1],"]", sep="")

list_to_str([1,2,3,4])


##Prob 3 - DONE
#lists_are_the_same(list1, list2), returns True iff list1 and list2 contain the same elements in the same order.

def lists_are_the_same(list1, list2):
    for i in range(0, len(list1)):
        if list1[i] != list2[i]:
            print("list item not the same")
        else:
            print("same")
lists_are_the_same([1,2,3,4],[1,2,4,3])


##Prob 4 - DONE
#simpify_fraction(n, m) which prints the simplified version of the fraction n/m
#ie. simpify_fraction(2, 6), print (1/2)
#Hint: use a similar technique to the one we used when determining whether a number is prime. That is, try dividing both the numerator and the denominator by every possible divisor in turn. For example, if you are simplifying 16/12, you can try dividing both by 16, 15, 14, ...., 1.

def simpify_fraction(n, m):
    if m % n == 0:
        m = int(m/n)
        n = int(n/n) #specify into so it doesn't return float
    print(str(n), "/", str(m), sep="")

simpify_fraction(4,8)

##Prob 5 - DONE
import math
pi = float(math.pi)
piCalc = pi * 10**15

sum = 0
terms = 100000
for t in range(terms+1):
    res = ((-1)**t)/(2*t + 1)
    sum += res
Lapprox = sum*4
LapproxCalc = Lapprox * 10**15


def find_same_sig_fig(x, y):
    sigfig = 0
    for i in range(15):
        a = x//10**(15-i)
        b = y//10**(15-i)
        if a == b:
            sigfig += 1
    return sigfig

print(find_same_sig_fig(LapproxCalc,piCalc))


##Prob 6 - DONE
#euclids algorithm: Given two numbers not prime to one another, to find their greatest common factor
#If A = 0 then GCD(A,B)=B, since the GCD(0,B)=B, and we can stop.
#If B = 0 then GCD(A,B)=A, since the GCD(A,0)=A, and we can stop.
#Write A in quotient remainder form (A = B⋅Q + R)
#Find GCD(B,R) using the Euclidean Algorithm since GCD(A,B) = GCD(B,R)

def euclids_alg(a,b):
    while a != 0:
        r = b % a
        b = a
        a = r
    print(b)

euclids_alg(1872,8493)




