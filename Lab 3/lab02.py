# Problem 1: Define get_current_value()
def get_current_value():
    return current_value

# ==================================================

def display_current_value():
    print("Current Value:", current_value)

def save_value():
    global prev_value
    prev_value = current_value

def add(to_add):
    global current_value
    save_value()
    if current_value != "ERROR":
        current_value += to_add

def subtract(to_subtract):
    global current_value
    save_value()
    if current_value != "ERROR":
        current_value -= to_subtract

def multiply(to_mult):
    global current_value
    save_value()
    if current_value != "ERROR":
        current_value *= to_mult

def divide(to_divide):
    global current_value
    save_value()
    if current_value != "ERROR":
        if to_divide == 0:
            current_value = 'ERROR'
        else:
            current_value /= to_divide

def store():
    global mem_value
    mem_value = current_value

def recall():
    global current_value
    current_value = mem_value

def undo():
    global current_value, prev_value
    current_value, prev_value = prev_value, current_value

def initialize():
    global current_value, prev_value, mem_value
    current_value = 0
    prev_value = 0
    mem_value = 0


if __name__ == '__main__':

    #+/-
    initialize()
    add(5)
    display_current_value() #expected output: 0+5=5


    current_value = 15
    subtract(7)

    display_current_value() #expected output: 15-7=8

    #+/-/*

    initialize()
    add(5)
    subtract(10)
    multiply(2)
    display_current_value()

    #negative number
    initialize()
    add(-5) #expected output: 0-5=-5


    #"irrational" number:
    import math
    current_value = 42
    divide(math.pi)
    display_current_value() #expected value: approx. 13.36901521971921


    #result 0
    initialize()
    add(5)
    subtract(5)
    display_current_value() # expected: 5-5 = 0
    #add 0
    current_value = 5
    add(0) #expected output: 5+0=0
    #/0
    current_value = 10
    divide(0)
    display_current_value() #expected output: ERROR
