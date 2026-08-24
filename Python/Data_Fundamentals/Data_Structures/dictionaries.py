# Acutis_Codes/Python/Data_Fundamentals/Data_Structures/dictionaries.py

"""
    Dictionaries are used to store data values in key:value pairs
    They are one of 4 built-in data types in Python used to store collections of data
    The other 3 are List, Tuple, and Set, all with different qualities and usage.
"""

# Initializing an empty dictionary
myDict = {}
myNestedDict = {
    "key1": 1, 
    "key2": {
        "nestedKey1": 2, 
        "nestedKey2": 3
        }
    }

myDict["key1"] = 1
myDict["key2"] = 2
myDict["key3"] = 3

print("Dictionary:", myNestedDict)