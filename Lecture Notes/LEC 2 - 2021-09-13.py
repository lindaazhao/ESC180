# Monday, Sep 13, 2021
# write a program that computes the roots of the equation ax^2+bx+c

import math

a = 1
b = 2
c = 1

disc = b**2 - 4 * a * c  # calculate discriminant
if disc > 0:  # 2 roots
    r1 = (-b - math.sqrt(disc))/(2*a)
    r2 = (-b + math.sqrt(disc))/(2*a)
    print(r1, r2, sep=", ")
elif disc == 0:
    print(-b/(2*a))
elif disc < 0:
    print("There are no roots.")

# writing a function


def my_add(a, b):
    res = a+b  # res = result
    return res


print(2*my_add(10, 12))
