import lab02

if __name__ == "__main__":
    lab02.initialize()
    lab02.add(23)
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
