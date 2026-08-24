# Acutis_Codes/Python/Loops/while.py

"""
    While loops are a control flow statement that allows you to execute a block of code repeatedly
    as long as a certain condition is true.

    Usage:
        while condition:
            # code block
    Example:
        x = 0
        while x < 5:
            print(x)
            x += 1
    
    use cases:
        1. To execute a block of code repeatedly until a certain condition is met
        2. To iterate over a collection of items, such as a list or a dictionary
        3. To create an infinite loop that runs until a certain condition is met
        4. To create a loop that runs until a user input is received
        5. To create a loop that runs until a certain event occurs, such as a button click or a timer expiration

    Incrementing and Decrementing:
        In a while loop, you can increment or decrement a variable to control the number of iterations

"""

# Implementation of while loop in python
x = 0

while x < 5:
    print("Iteration:", x)
    print(x)
    x += 1

separator = "-" * 20
print(separator)
# Do while loop in python
x = 0

while True:
    print("Iteration:", x)
    print(x)
    x += 1
    if x >= 5:
        break
