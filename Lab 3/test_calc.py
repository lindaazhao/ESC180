import lab02

if __name__ == "__main__":
    lab02.initialize()
    lab02.add(5)
    if (lab02.get_current_value() == 5): #current_value = 5
        print("Test1 passed!")
    else:
        print("Test1 failed!")

    lab02.initialize()
    lab02.multiply(3)
    if (lab02.get_current_value() == 5): #current_value = 0
        print("Test2 passed!")
    else:
        print("Test2 failed!")
