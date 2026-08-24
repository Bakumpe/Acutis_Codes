# Acutis_Codes/Python/Functional_Programming/Higher_Order/higher.py

"""
    Higher-Order Functions

    A higher-order function is a function that does at least one of the following:
        1. Takes one or more functions as arguments.
        2. Returns a function as its result.

    This is possible in Python because functions are "first-class objects" —
    they can be assigned to variables, stored in data structures, passed as
    arguments, and returned from other functions, just like any other value.
"""


# 1. Functions as first-class objects
def shout(text):
    return text.upper() + "!"


say = shout                # assign function to a variable
print(say("hello"))        # HELLO!


# 2. Passing a function as an argument
def apply_twice(func, value):
    return func(func(value))


print(apply_twice(shout, "hi"))   # HI!!


# 3. Built-in higher-order functions: map, filter, reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda n: n ** 2, numbers))
print(squared)                     # [1, 4, 9, 16, 25]

evens = list(filter(lambda n: n % 2 == 0, numbers))
print(evens)                       # [2, 4]

total = reduce(lambda acc, n: acc + n, numbers)
print(total)                       # 15


# 4. Returning a function (a "closure")
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier


double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))   # 10
print(triple(5))   # 15


# 5. Custom sort with a function argument
words = ["banana", "kiwi", "apple", "fig"]
by_length = sorted(words, key=len)
print(by_length)   # ['fig', 'kiwi', 'apple', 'banana']


# 6. Decorators: functions that take and return functions
print("Decorators")
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}({args}, {kwargs})")
        return func(*args, **kwargs)
    return wrapper


@log_call
def add(a, b):
    return a + b

@log_call
def sub(a,b):
    return a - b


print(add(2, 3))
print(sub(4, 5))
# Calling add((2, 3), {})
# 5