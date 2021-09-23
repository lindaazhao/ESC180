# Test
def display_current_value(): #2.Display CV
    print("Current value:", current_value)

def add(to_add): # 3. Addition #4.Global
    global current_value
    current_value = current_value + to_add
    value_list.append(current_value)

def subtract(to_subtract):
    global current_value
    current_value = current_value - to_subtract
    value_list.append(current_value)

def multiply(multiply_by): #5
    global current_value
    current_value = current_value*multiply_by
    value_list.append(current_value)

def divide(divide_by): #5
    global current_value
    current_value = current_value/to_divide #<-- returns a float
    #current_value = current_value//to_divide <-- returns a whole number
    value_list.append(current_value)

def remember():
    global memory
    memory = current_value

def recall():
    global current_value
    current_value = memory

def undo():
    global current_value
    num_values = len(value_list)
    current_value = value_list[num_values - 2]
    value_list.pop(num_values-1)

value_list = [0]

if __name__ == "__main__":
    current_value = 0
    print("Welcome to the calculator program.\nCurrent value:",  str(current_value)) #1.Welcome

    display_current_value() # 0
    add(5) # 5
    print(value_list)
    subtract(2)
    print(value_list)
    display_current_value() # 3
    undo()
    print(value_list)
    display_current_value() # 5
    undo()
    print(value_list)
    display_current_value() # 0
    add(2)
    print(value_list)
    display_current_value()

## organization needed - claire


