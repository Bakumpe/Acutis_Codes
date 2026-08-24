# Statements vs. Expressions in Python

"""
    In Python, statements and expressions are two fundamental concepts that are used to write code.
    A statement is a line of code that performs an action, such as assigning a value to a variable
    or calling a function.
    An expression is a line of code that evaluates to a value, such as a mathematical operation or
    a function call that returns a value.

    In Python, statements are executed for their side effects, while expressions are evaluated for
    their value. This means that statements can change the state of the program, while expressions
    cannot.
"""

# Statement
x = 5                  # assignment statement
if x > 0:               # if statement
    print("positive")
for i in range(3):      # for statement
    print(i)
    
def greet():            # function definition statement
    return "hi"

import math              # import statement

# Expressions
5 + 3                    # arithmetic expression -> 8
x > 0                     # comparison expression -> True
greet()                   # function call expression -> "hi"
[i for i in range(3)]     # list comprehension expression -> [0, 1, 2]

"hello".upper()           # method call expression -> "HELLO"