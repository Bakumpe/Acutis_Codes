# Acutis_Codes/Python/Control_Flows/Statements_vs_Expressions/statements_vs_expressions.py
"""
    Statements vs. Expressions

    A statement is a line of code that performs an action - it does
    something, but doesn't itself produce a usable value (assigning a
    variable, running an if/for/while, defining a function, importing a
    module).

    An expression is a line of code that evaluates to a value - it can be
    printed, assigned, or passed to a function (arithmetic, comparisons,
    function calls that return something, comprehensions).

    Rule of thumb: if you can put it on the right-hand side of `x = ___` or
    pass it to print(), it's an expression. If it changes the state of the
    program instead of producing a value, it's a statement.
"""

# --- Statements: run for their side effects, not for a value ---
x = 5                    # assignment statement
if x > 0:                # if statement
    print("positive")
for i in range(3):       # for statement
    print(i)

def greet():              # function definition statement
    return "hi"

import math                # import statement


# --- Expressions: evaluated to produce a value ---
print(5 + 3)                  # arithmetic expression -> 8
print(x > 0)                   # comparison expression -> True
print(greet())                  # function call expression -> "hi"
print([i for i in range(3)])     # list comprehension expression -> [0, 1, 2]
print("hello".upper())            # method call expression -> "HELLO"


# --- Where the line blurs: the walrus operator (Python 3.8+) ---
# `:=` is an assignment EXPRESSION: it assigns a value AND evaluates to that
# value at the same time, so - unlike a plain `=` assignment statement - it
# can be used inside another expression, such as an if condition.
data = [1, 2, 3, 4, 5]
if (n := len(data)) > 3:
    print(f"data has {n} items, which is more than 3")