# Acutis_Codes/Python/Data_Fundamentals/Type_Systems/types.py

"""
    Python is a dynamically typed language, which means that you don't have to declare the
     type of a variable when you create one.
    The interpreter infers the type of the variable based on the value assigned to it.

    However, Python also supports static typing through type hints, which allow you to 
    specify the expected type of a variable or function parameter.
    This can help catch errors early and improve code readability.

    In this file, we will explore the different types in Python and how to use them effectively.

    Types in Python can be broadly categorized into the following categories:
        1. Numeric Types: int, float, complex
        2. Sequence Types: list, tuple, range
        3. Text Type: str
        4. Set Types: set, frozenset
        5. Mapping Type: dict
        6. Boolean Type: bool
        7. Binary Types: bytes, bytearray, memoryview
"""

# Numeric Types
x = 5  # int
y = 3.14  # float
z = 2 + 3j  # complex

# Sequence Types
myList = [1, 2, 3]  # list
myTuple = (1, 2, 3)  # tuple
myRange = range(5)  # range

# Text Type
myString = "Hello, World!"  # str

# Set Types
mySet = {1, 2, 3}  # set
myFrozenSet = frozenset([1, 2, 3])  # frozenset

# Mapping Type
myDict = {"name": "John", "age": 30}  # dict

# Boolean Type
myBool = True  # bool

# Binary Types
myBytes = b"Hello"  # bytes
myBytearray = bytearray(b"Hello")  # bytearray
myMemoryView = memoryview(b"Hello")  # memoryview


