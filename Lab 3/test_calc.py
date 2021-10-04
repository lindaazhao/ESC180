import lab02
from lab02 import * # **(Maybe) don't do this :^), 
# **but it allows you to use functions from lab02 without writing "lab02." before calling the function

if __name__ == "__main__":
    lab02.initialize()
    lab02.add(23)

    # **This will pop an error if it is false, so it's a good way to check things that should be true
    assert lab02.get_current_value == 23, "Test 1 failed"

    if (lab02.get_current_value() == 23): #test if current_value = 23
        print("Test 1 passed!")
    else:
        print("Test 1 failed!")

    lab02.undo()
    if (lab02.get_current_value() == 0): #test if current_value = 0
        print("Test 2 passed!")
    else:
        print("Test 2 failed!")


    lab02.initialize()
    lab02.multiply(3)
    if (lab02.get_current_value() == 0): #test if current_value = 0
        print("Test 3 passed!")
    else:
        print("Test 3 failed!")
