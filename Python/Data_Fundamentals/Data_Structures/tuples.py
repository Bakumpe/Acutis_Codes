# Acutis_Codes/Python/Data_Fundamentals/Data_Structures/tuples.py

# Tuples are used to store multiple items in a single variable
# They are one of 4 built-in data types in Python used to store collections of data
# The other 3 are List, Set, and Dictionary, all with different qualities and usage.

""""
Usage:
    1. Tuples are created using parentheses ()
    2. Tuples can contain items of different data types
    3. Tuples are immutable, meaning that their elements cannot be changed after they are created
    4. Tuples can be nested, meaning that they can contain other tuples as elements
    5. Tuples can be iterated over using loops
    6. Tuples can be sliced, meaning that a portion of the tuple can be extracted
    7. Tuples can be concatenated, meaning that two or more tuples can be combined into a single tuple
    8. Tuples can be repeated, meaning that a tuple can be multiplied by an integer to create a new tuple with repeated elements
Use Cases:
    1. Tuples are used to store multiple items in a single variable
    2. Tuples are used to store items of different data types
    3. Tuples are used to store items that cannot be changed after they are created
    4. Tuples are used to store items that can be nested
    5. Tuples are used to store items that can be iterated over using loops
    6. Tuples are used to store items that can be sliced
    7. Tuples are used to store items that can be concatenated
    8. Tuples are used to store items that can be repeated
"""
separator = "-" * 70
spaces = " " * 10

# Implementation of tuples in python

# Initializing an empty tuple
myTuple = ()

# Tuples can contain items of different data types
myMixedTuple = (1, "Hello", 3.14, True)

# Tuples can be nested, meaning that they can contain other tuples as elements
myNestedTuple = (1, 2, (3, 4), 5)

# Tuples can be iterated over using loops
print(separator)
for item in myMixedTuple:
    print(item)

