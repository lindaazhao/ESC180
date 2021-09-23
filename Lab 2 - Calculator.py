# Problem 1 located below (line 68)

# Problem 2: Display Current Value
def display_current_value():
    print("Current value:", current_value)


# Problem 3: Addition; Problem 4: Global Variable
def add(to_add):
    global current_value, prev_value
    prev_value = current_value
    current_value += to_add
    value_list.append(current_value)

def subtract(to_subtract):
    global current_value, prev_value
    prev_value = current_value
    current_value -= to_subtract
    value_list.append(current_value)


# Problem 5: Multiplication & Division
def multiply(multiply_by):
    global current_value, prev_value
    prev_value = current_value
    current_value *= multiply_by
    value_list.append(current_value)

def divide(divide_by):
    global current_value, prev_value
    prev_value = current_value
    if divide_by == 0:
        current_value = "Error"
    else:
        current_value /= divide_by # <-- returns a float
    #current_value = current_value//divide_by <-- returns a whole number
    value_list.append(current_value)


# Problem 6: Memory and Recall
def remember():
    global memory
    memory = current_value

def recall():
    global current_value
    current_value = memory


# Problem 7: Undo
def undo1(): # initial solution; back only, doesn't undo the previous undo
    global current_value
    num_values = len(value_list)
    current_value = value_list[num_values - 2]
    value_list.pop(num_values-1)

def undo2(): # works as stated in problem
    global current_value, prev_value
    temp = current_value
    current_value = prev_value
    prev_value = temp


def clear(): # Clears the calculator, resetting current_value and prev_value
    global current_value, prev_value, value_list
    current_value = 0
    prev_value = 0
    value_list = [0]

    
# ==================================================================================

if __name__ == "__main__":
    # Problem 1: Welcome Message
    clear()
    print("Welcome to the calculator program.\nCurrent value:",  str(current_value))

    # Running Tests
    display_current_value() # 0
    add(5) # 5
    print(value_list)
    subtract(2)
    print(value_list)
    display_current_value() # 3
    undo1()
    print(value_list)
    display_current_value() # 5
    undo1()
    print(value_list)
    display_current_value() # 0
    add(2)
    print(value_list)
    display_current_value()
    remember() # remember 2
    multiply(5)
    subtract(1)
    display_current_value() # 9
    undo2() 
    display_current_value() #10
    undo2() 
    display_current_value() #9
    recall()
    display_current_value() # 2


