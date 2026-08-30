# Acutis_Codes/Python/Data_Fundamentals/Type_Systems/typesSystem.py

"""
TYPE SYSTEMS

Python is a dynamically typed language -- you don't declare a variable's
type when you create it. The interpreter figures out the type from the
value you assign, and that type can even change later if you reassign
the variable to something else.

Python is also strongly typed -- it will NOT silently convert between
incompatible types for you. "5" + 5 raises an error instead of guessing
what you meant. This is different from a "weakly typed" language, which
might quietly coerce "5" + 5 into 10 or "55" without telling you.

Python also supports optional static type hints, which let you annotate
the expected type of a variable or function parameter. Type hints don't
change how the code runs (Python ignores them at runtime) -- they exist
to help humans and tools like mypy catch mistakes before you ever run
the program.

Types in Python fall into these broad categories:
    1. Numeric Types:  int, float, complex
    2. Sequence Types: list, tuple, range
    3. Text Type:      str
    4. Set Types:      set, frozenset
    5. Mapping Type:   dict
    6. Boolean Type:   bool
    7. Binary Types:   bytes, bytearray, memoryview

This file tours all seven, then demonstrates what "dynamically typed"
and "strongly typed" actually mean in practice.
"""


# ---------------------------------------------------------------------------
# 1. Numeric Types
# ---------------------------------------------------------------------------
my_int = 5              # int -- whole number
my_float = 3.14          # float -- decimal number
my_complex = 2 + 3j      # complex -- has a real and imaginary part

print("my_int:", my_int, "| type:", type(my_int))
print("my_float:", my_float, "| type:", type(my_float))
print("my_complex:", my_complex, "| type:", type(my_complex))


# ---------------------------------------------------------------------------
# 2. Sequence Types
# ---------------------------------------------------------------------------
my_list = [1, 2, 3]      # list -- ordered, mutable
my_tuple = (1, 2, 3)     # tuple -- ordered, immutable
my_range = range(5)      # range -- a lazy sequence of numbers (0..4 here)

print("\nmy_list:", my_list, "| type:", type(my_list))
print("my_tuple:", my_tuple, "| type:", type(my_tuple))
print("my_range:", list(my_range), "| type:", type(my_range))
# Note: range doesn't store all its numbers in memory at once -- it
# generates them on demand, which is why we convert it to a list to print it.


# ---------------------------------------------------------------------------
# 3. Text Type
# ---------------------------------------------------------------------------
my_string = "Hello, World!"   # str

print("\nmy_string:", my_string, "| type:", type(my_string))


# ---------------------------------------------------------------------------
# 4. Set Types
# ---------------------------------------------------------------------------
my_set = {1, 2, 3}                  # set -- unordered, mutable, no duplicates
my_frozenset = frozenset([1, 2, 3])  # frozenset -- same as set, but immutable

print("\nmy_set:", my_set, "| type:", type(my_set))
print("my_frozenset:", my_frozenset, "| type:", type(my_frozenset))

# A frozenset can't be changed after creation -- this is why it's
# hashable and can be used as a dict key or stored inside another set,
# while a regular set cannot.
# my_frozenset.add(4)   # uncomment to see: AttributeError, add() doesn't exist


# ---------------------------------------------------------------------------
# 5. Mapping Type
# ---------------------------------------------------------------------------
my_dict = {"name": "John", "age": 30}   # dict -- key/value pairs

print("\nmy_dict:", my_dict, "| type:", type(my_dict))


# ---------------------------------------------------------------------------
# 6. Boolean Type
# ---------------------------------------------------------------------------
my_bool = True   # bool -- True or False

print("\nmy_bool:", my_bool, "| type:", type(my_bool))


# ---------------------------------------------------------------------------
# 7. Binary Types
# ---------------------------------------------------------------------------
my_bytes = b"Hello"                    # bytes -- immutable sequence of raw bytes
my_bytearray = bytearray(b"Hello")     # bytearray -- mutable version of bytes
my_memoryview = memoryview(b"Hello")   # memoryview -- a view over another object's
                                        #   bytes, without copying them

print("\nmy_bytes:", my_bytes, "| type:", type(my_bytes))
print("my_bytearray:", my_bytearray, "| type:", type(my_bytearray))
print("my_memoryview:", bytes(my_memoryview), "| type:", type(my_memoryview))

# bytearray is mutable -- you can change individual bytes in place.
my_bytearray[0] = ord("Y")   # ord("Y") gives the numeric byte value for "Y"
print("my_bytearray after edit:", my_bytearray)

# bytes is not -- this would raise a TypeError if uncommented:
# my_bytes[0] = ord("Y")


# ---------------------------------------------------------------------------
# Dynamic typing in action
# ---------------------------------------------------------------------------
# The same variable can hold different types over its lifetime, because
# Python attaches the type to the VALUE, not to the variable name itself.
dynamic_example = 10
print("\ndynamic_example:", dynamic_example, "| type:", type(dynamic_example))

dynamic_example = "now I'm a string"
print("dynamic_example:", dynamic_example, "| type:", type(dynamic_example))

dynamic_example = [1, 2, 3]
print("dynamic_example:", dynamic_example, "| type:", type(dynamic_example))


# ---------------------------------------------------------------------------
# Strong typing in action
# ---------------------------------------------------------------------------
# Python won't silently mix incompatible types -- it raises an error
# instead of guessing what you meant. Uncomment the line below to see it:
#
# result = "5" + 5   # TypeError: can only concatenate str (not "int") to str
#
# You have to be explicit about the conversion:
result = "5" + str(5)
print("\n'5' + str(5) =", result)

result = int("5") + 5
print("int('5') + 5 =", result)


# ---------------------------------------------------------------------------
# Optional static typing: type hints
# ---------------------------------------------------------------------------
# Type hints document the type you INTEND a variable or function to use.
# Python does not enforce them at runtime -- they're for readability and
# for external tools (like mypy or your editor) to catch mistakes early.

age: int = 30            # a variable hint
username: str = "ada"

def add_numbers(a: int, b: int) -> int:
    """Add two integers and return an integer."""
    return a + b

print("\nadd_numbers(2, 3):", add_numbers(2, 3))

# Python will NOT stop you from breaking the hint at runtime -- this
# still runs without error, even though it violates the type hint:
print("add_numbers('2', '3'):", add_numbers("2", "3"))   # returns "23", not 5
# A type checker like mypy would flag this line as an error before you
# ever run the program. Python itself just shrugs and does what you asked.


# ---------------------------------------------------------------------------
# Try it yourself
# ---------------------------------------------------------------------------
# 1. Reassign one variable to three different types in a row (like
#    dynamic_example above) and print type() after each reassignment.
# 2. Uncomment "5" + 5 and read the TypeError Python raises -- this is
#    strong typing enforcing itself.
# 3. Write a function with type hints, then deliberately call it with
#    the wrong type. Notice Python runs it anyway -- hints are a
#    convention, not a rule the interpreter enforces.