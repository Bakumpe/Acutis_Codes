# Acutis_Codes/Python/Functional_Programming/Immutability/immutability.py

"""
    Immutability

    An immutable object is one whose state cannot be changed after it is
    created. Functional programming favors immutability because it avoids
    "side effects" — unexpected changes to shared data — which makes code
    easier to reason about, test, and run safely across multiple threads.

    Python has both immutable and mutable built-in types:

        Immutable: int, float, bool, str, tuple, frozenset, bytes
        Mutable:   list, dict, set, bytearray

    "Immutable" means the object itself cannot be changed in place —
    operations that look like they modify it actually create a new object.
"""


# 1. Immutable example: strings
s = "hello"
s_upper = s.upper()
print(s)          # hello        (unchanged)
print(s_upper)    # HELLO        (a new string was created)
print(id(s) == id(s_upper))   # False -> different objects


# 2. Immutable example: tuples
point = (1, 2)
try:
    point[0] = 99
except TypeError as e:
    print(f"Error: {e}")   # 'tuple' object does not support item assignment


# 3. Mutable example: lists (for contrast)
nums = [1, 2, 3]
nums.append(4)
print(nums)        # [1, 2, 3, 4]  -> changed in place, same object


# 4. Why immutability matters: avoiding side effects
def add_item_bad(item, target_list=[]):   # classic Python pitfall!
    target_list.append(item)
    return target_list


print(add_item_bad("a"))   # ['a']
print(add_item_bad("b"))   # ['a', 'b']  -> unexpected! default list was reused


def add_item_good(item, target_list=None):
    target_list = list(target_list) if target_list else []
    target_list.append(item)
    return target_list


print(add_item_good("a"))   # ['a']
print(add_item_good("b"))   # ['b']  -> no leftover state


# 5. Working immutably with functions instead of mutation
original = [1, 2, 3]
doubled = list(map(lambda n: n * 2, original))
print(original)   # [1, 2, 3]   (untouched)
print(doubled)     # [2, 4, 6]  (new list)


# 6. frozenset: an immutable version of set
mutable_set = {1, 2, 3}
frozen = frozenset(mutable_set)
try:
    frozen.add(4)
except AttributeError as e:
    print(f"Error: {e}")   # 'frozenset' object has no attribute 'add'


# 7. Simulating immutable "records" with NamedTuple
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


p1 = Point(1, 2)
p2 = p1._replace(x=99)   # creates a NEW Point instead of mutating p1
print(p1)   # Point(x=1, y=2)
print(p2)   # Point(x=99, y=2)


# 8. dataclasses can also be made immutable
from dataclasses import dataclass


@dataclass(frozen=True)
class Vector:
    x: float
    y: float


v = Vector(1.0, 2.0)
try:
    v.x = 5.0
except AttributeError as e:
    print(f"Error: {e}")   # cannot assign to field 'x'