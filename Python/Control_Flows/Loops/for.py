# Acutis_Codes/Python/Control_Flows/Loops/for.py

"""
    For loops are a control flow statement that allows you to iterate over a sequence of values.
    In Python, for loops are typically used to iterate over a list, tuple, or string.

    Usage:
        for variable in sequence:
            # code block
    Example:
        for i in range(5):
            print(i)
    Use Cases:
        1. To iterate over a sequence of values, such as a list, tuple, or string
        2. To execute a block of code a certain number of times
        3. To iterate over a collection of items, such as a list or a dictionary
    Incrementing and Decrementing:
        In a for loop, you can increment or decrement a variable to control the number of iterations

"""

# Implementation of for loop in python

for i in range(5):
    print("Iteration:", i)
    print(i)

# Implementation of for loop in python using a list
my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print("Item:", item)
    print(item)