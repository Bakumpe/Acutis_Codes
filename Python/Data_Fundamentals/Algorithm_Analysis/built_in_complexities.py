# Acutis_Codes/Python/Data_Fundamentals/Algorithm_Analysis/built_in_complexities.py

"""
COMPLEXITY OF PYTHON'S BUILT-IN METHODS

big_o_notation.py covers what O(1), O(n), O(n^2), etc. MEAN. This file
covers something more practical: the actual complexity of the built-in
methods you already use constantly -- .append(), .pop(), .sort(), "in",
and their equivalents on dict and set.

You don't need to memorize a textbook's worth of these. You need enough
to answer one question while you're coding: "is the method I'm about
to call in a loop going to make this slow?" That's the entire point of
this file.

n below always means "the number of items in the collection."
"""


# ---------------------------------------------------------------------------
# list -- most operations depend on WHERE you're working: front vs. back
# ---------------------------------------------------------------------------
"""
Method / operation      Complexity   Why
-----------------------------------------------------------------------
list[i]                 O(1)         direct index into memory, no searching
list.append(x)          O(1)         adds to the end, no shifting needed
list.pop()               O(1)        removes from the end, no shifting needed
list.pop(0)              O(n)        removes from the front -- every other
                                       item must shift left by one
list.insert(0, x)        O(n)        inserting at the front shifts everything
x in list                O(n)        must check items one by one until found
list.index(x)            O(n)        same reason as "in" -- linear scan
list.sort()               O(n log n)  Python uses Timsort, a hybrid of merge
                                       sort and insertion sort
len(list)                 O(1)        Python tracks the length, doesn't count
"""

my_list = [5, 3, 8, 1, 9, 2]

print("my_list:", my_list)
print("my_list[0] (O(1)):", my_list[0])

my_list.append(100)          # O(1)
print("after append(100):", my_list)

my_list.pop()                 # O(1) -- removes from the end
print("after pop():", my_list)

my_list.pop(0)                 # O(n) -- removes from the front, shifts everything
print("after pop(0):", my_list)

print("8 in my_list (O(n)):", 8 in my_list)

my_list.sort()                 # O(n log n)
print("after sort():", my_list)

# This is exactly why queues.py steered you toward collections.deque
# instead of a list: a queue removes from the front constantly, and
# list.pop(0) being O(n) means that cost gets paid on every single
# removal.


# ---------------------------------------------------------------------------
# dict -- built on a hash table, so most operations are O(1) on average
# ---------------------------------------------------------------------------
"""
Method / operation       Complexity     Why
-----------------------------------------------------------------------
dict[key]                 O(1) average   the key's hash points almost
                                          directly to its value's location
dict[key] = value          O(1) average   same reasoning, for inserts
key in dict                O(1) average   checks the hash table, not every
                                          key one by one
dict.pop(key)               O(1) average   same hash-based lookup, then remove
dict.keys() / .values()      O(1)           these return VIEWS, not copies --
  / .items()                                creating them doesn't scan anything
len(dict)                   O(1)           tracked directly, like list

"O(1) average" (not "always") because hash collisions can occasionally
make a single lookup slower -- but this is rare enough in practice that
dict lookups are treated as constant time for everyday reasoning.
"""

my_dict = {"a": 1, "b": 2, "c": 3}

print("\nmy_dict:", my_dict)
print("my_dict['b'] (O(1) avg):", my_dict["b"])
print("'z' in my_dict (O(1) avg):", "z" in my_dict)

my_dict["d"] = 4               # O(1) average
print("after my_dict['d'] = 4:", my_dict)

# Compare this to searching for a value inside a LIST of the same size
# with "in" -- that's O(n). This is the single biggest reason to reach
# for a dict instead of a list when you need to look things up by key
# rather than by position.


# ---------------------------------------------------------------------------
# set -- also a hash table under the hood, same profile as dict
# ---------------------------------------------------------------------------
"""
Method / operation       Complexity     Why
-----------------------------------------------------------------------
x in set                  O(1) average   hash-based lookup, same as dict
set.add(x)                 O(1) average   hash-based insert
set.remove(x)                O(1) average   hash-based lookup, then remove
"""

my_set = {1, 2, 3, 4, 5}

print("\nmy_set:", my_set)
print("3 in my_set (O(1) avg):", 3 in my_set)
print("3 in [1, 2, 3, 4, 5] (O(n)):", 3 in [1, 2, 3, 4, 5])
# Both lines above give the same answer (True), but the set version
# doesn't get slower as the collection grows -- the list version does.
# This is why sets.py's "fast membership checks" claim (from the
# README) is a Big-O claim, not just a convenience claim.


# ---------------------------------------------------------------------------
# str -- text has its own quirks worth knowing
# ---------------------------------------------------------------------------
"""
Method / operation       Complexity   Why
-----------------------------------------------------------------------
len(string)                O(1)         tracked directly, like list/dict
string[i]                  O(1)         direct index, same as list
substring in string          O(n)         has to scan for a match
string.split()               O(n)         must walk the whole string once
"a" + "b" (concatenation)      O(n)         strings are immutable -- each "+"
                                            builds an entirely NEW string by
                                            copying both originals

The concatenation cost is easy to miss: building up a long string with
"+=" inside a loop is quietly O(n^2) overall, because each "+=" copies
everything accumulated so far. "".join(list_of_strings) avoids this --
it builds the result once, in O(n) total.
"""

parts = ["Hello", " ", "World", "!"]

# The slow way (still fine for a handful of pieces, but scales badly):
slow_result = ""
for part in parts:
    slow_result += part   # O(n) per concatenation -> O(n^2) overall for many parts
print("\nslow_result:", slow_result)

# The fast way:
fast_result = "".join(parts)   # O(n) total
print("fast_result:", fast_result)


# ---------------------------------------------------------------------------
# Try it yourself
# ---------------------------------------------------------------------------
# 1. Time both concatenation approaches above on a list of 100,000
#    short strings (use Python's `time` module). Confirm "".join() is
#    dramatically faster than repeated "+=".
# 2. Write a function that checks whether a value exists in a
#    collection, once using a list and once using a set built from the
#    same data. Time both against a large collection and confirm the
#    set version stays roughly flat as the collection grows, while the
#    list version gets slower.
# 3. Go back to Abstract_Data_Structures/queues.py and stacks.py and
#    match each operation used there (append, pop, pop(0), popleft) to
#    its row in the list section above.