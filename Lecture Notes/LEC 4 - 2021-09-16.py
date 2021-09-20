# Multiple Assignment
# a = b  # assignment
# a1, a2 = b1, b2  # same as above, put b1 in a1, put b2 in a2

a = 3
b = 4

a, b = b, a  # swap values for a and b

# can't translate this to
a = b
b = a  # this will set both values to 4

# Swap values of a and b without multiple assignment
temp = a  # temp as the old value of a, a has the old value of a, and b has the old value of b
a = b  # temp still has the old value of a, a has the old value of b, b unchanged
b = temp  # a has old value of b, b has old value of a

# 2 integers, a and b, swap their values without multiple assignment & without using extra variable
b = a + b
a = b - a  # think about this and figure it out lol


# Converting Objects to Different Types
# int, float, str, bool
int(3.14)  # gets rid of the fractional part; no rounding
# 3.14, 3,75 --> 3
str(3.14)  # converts to '3.14'
# cannot add string and float normally
s2 = 'The value of pi is approx ' + str(3.14)
print(s2)

bool('asdf')  # True (as long as not empty string)
bool('zero')
bool('')  # False
bool(0)  # False

int("35")  # --> 35
float("35.4")  # --> 35.4
# int("123.45")  # Error, string is not a valid integer
print(int(float("123.45")))  # This is valid

int(True)  # --> 1
int(False)  # --> 0

# Ctrl + Alt + N to run highlighted code

# manipulation of global variables within a function will affect everything outside of the function;
# there is no local variable in addition to the global one

a = 5
a + 2  # this just tells python '7'
print(a)  # this will print 5
