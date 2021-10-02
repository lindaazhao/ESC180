## Lab 1: Tracing and Conditionals (hello)
## September 18, 2021
## ==================================================

# Problem 1
print("Hello, Python")

# Problem 2
print("Hello, Claire")
print("Hello, Linda")

# Problem 3
name1 = "Claire"
name2 = "Linda"

print("Hello, " + name1 + " and " + name2 + ". Your names are " + name1 + " and " +
      name2 + ". Hi there. Your names are still " + name1 + " and " + name2 + ".")

# Problem 4
name1 = "Prof. Cluett"
name2 = "Prof. Thywissen"
# Visual confirmation that variable values changed
# print("Hello, " + name1 + " and " + name2)

# Problem 5
greetee = str(input("What is your name?: "))
if greetee == "Lord Voldemort":
    print("I'm not talking to you.")
else:
    print("Hello, " + greetee)
