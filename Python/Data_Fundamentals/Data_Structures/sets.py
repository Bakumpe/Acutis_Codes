# Acutis_Codes/Python/Data_Fundamentals/Data_Structures/sets.py

"""
    Sets are used to store multiple items in a single variable
    They are one of 4 built-in data types in Python used to store collections of data
    The other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

"""

# Initializing an empty set
# mySet = set()
# mySet.add(1)
mySet = {1, 2, 3, 4, 5}
myMixedSet = {1, "Hello", 3.14, True}
myNestedSet = {1, 2, frozenset({3, 4}), 5}

print("Set:", mySet)