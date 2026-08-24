# Acutis_Codes/Python/Control_Flows/Branching/branching.py
"""
    Branching is a control flow statement that allows you to execute different code 
    blocks based on certain conditions.
    In Python, branching is typically done using if, elif, and else statements.

    Usage:
        if condition:
            # code block
        elif another_condition:
            # code block
        else:
            # code block

    Example:
        x = 10
        if x > 5:
            print("x is greater than 5")
        elif x == 5:
            print("x is equal to 5")
        else:
            print("x is less than 5")

    Use Cases:
        1. To execute different code blocks based on certain conditions
        2. To make decisions in your code based on user input or other factors
        3. To handle different scenarios in your code, such as error handling or input validation
        4. To create more complex logic in your code by combining multiple conditions using 
        logical operators.
        5. To create more readable and maintainable code by breaking down complex logic into smaller,
        more manageable pieces using branching statements.

            
"""

# Implementation of branching in python
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# Implementation of branching in python using logical operators
y = 20
if y > 10 and y < 30:
    print("y is between 10 and 30")



