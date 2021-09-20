# Tuesday, Sep 14, 2021
# Types of Variables

import math

# Integer type
a = 5
print(type(a))
print(type(6))
print(type(4//2))  # integer division
print(type(7//2))

# Float type
print(type(4/2))  # float division

# Text type
# want to print '"line one <line break> line two"'
s = "line one \nline two"
print(s)
# can't print "artsies are "smart"", need to use different types of quotations
# ex. print("artsies are 'smart'")

# Boolean type
# can be True or False
a = (6 > 5)
print(a)
b = (2 == 3)
print(b)

# "collectively you paid like 100s of thousands of dollars and tech support is not answering. sorry about that."
# - prof. guerzhoy on when the projector doesn't work

a = math.sqrt(9)
print(a)


def pirate_print(s):
    print("Ahoy! " + s + " Arr!")


pirate_print("I <3 Praxis")

# below is a better function than the first
# this is because it doesn't actually immediately **do** anything (which we like)
# called a derived function


def piratify(s):
    return "Ahoy! " + s + " Arr!"


print(piratify(piratify("Calc")))


# quadratic roots solver
def has_roots(a, b, c):
    """ return True iff ax^2+bx+c=0 has at least one real root"""
    # this is called a docstring; does not get ignored like a comment;
    # string that describes what a function does

    # since disc is defined in the function, it is called a local variable; only exists while the function is running
    # cannot retrieve value of disc outside of function after calling it
    disc = b**2 - 4*a*c
    # if disc >= 0:
    #     return True
    # else:
    #     return False
    return disc >= 0


help(has_roots)
# will "print" the docstring to tell what the function is


# example of a local variable;
# "print(grade)" line will print 97 because the grade = 79 is only a local variable, not global
def plunder_grade():
    global grade  # sets grade to a global variable
    grade = 79
    print(grade)


grade = 97
plunder_grade()  # resets global grade variable to 79
print(grade)


# intro to program spanning multiple files
def f(x):
    return x**2


if __name__ == __main__:
    print(f(s))
