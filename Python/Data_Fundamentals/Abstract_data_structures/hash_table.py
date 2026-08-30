# Acutis_Codes/Python/Data_Fundamentals/Abstract_Data_Structures/hash_table.py

"""
HASH TABLES

Python's dict and set are hash tables -- but they're built-in and
ready to use, which hides HOW they achieve O(1) average lookup. This
file builds a basic hash table from scratch, using nothing but a
plain list, so you can see the mechanism dict and set are hiding from you.

The core idea:
    1. Take a key (e.g. "apple").
    2. Run it through a HASH FUNCTION, which turns it into a number.
    3. Use that number (mod the table size) to pick a "bucket" -- an
       index in a list -- where the key/value pair will live.
    4. To look the key up again, hash it the SAME way, jump straight
       to that bucket, and look inside it.

Because step 2 and 3 don't depend on how many keys are already stored,
a lookup costs roughly the same whether the table holds 5 items or
5 million -- that's where "O(1) average" comes from.

The "average" matters because two different keys can sometimes hash to
the SAME bucket -- this is called a COLLISION. This file handles
collisions with CHAINING: each bucket holds a small list, so multiple
key/value pairs can share a bucket without overwriting each other.
"""


class HashTable:
    def __init__(self, size=8):
        # Each slot in this list is a "bucket" -- itself a list of
        # [key, value] pairs. Starting with an empty list per bucket
        # is what makes chaining possible.
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        # Python's built-in hash() turns almost any immutable value
        # into a large integer. We shrink that number down to fit our
        # bucket list with modulo -- this is the "which bucket does
        # this key belong in?" step.
        return hash(key) % self.size

    def set(self, key, value):
        bucket = self.buckets[self._hash(key)]
        # If the key already exists in this bucket, update it instead
        # of adding a duplicate entry.
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])

    def get(self, key):
        bucket = self.buckets[self._hash(key)]
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        raise KeyError(key)

    def remove(self, key):
        bucket = self.buckets[self._hash(key)]
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(i)
                return
        raise KeyError(key)

    def __contains__(self, key):
        bucket = self.buckets[self._hash(key)]
        return any(pair[0] == key for pair in bucket)

    def __repr__(self):
        return str(self.buckets)


# ---------------------------------------------------------------------------
# Using the hash table
# ---------------------------------------------------------------------------
table = HashTable()

table.set("apple", 1)
table.set("banana", 2)
table.set("cherry", 3)

print("get('banana'):", table.get("banana"))
print("'apple' in table:", "apple" in table)
print("'mango' in table:", "mango" in table)

table.set("apple", 100)   # updates the existing key, doesn't duplicate it
print("get('apple') after update:", table.get("apple"))

table.remove("cherry")
print("'cherry' in table after remove:", "cherry" in table)

try:
    table.get("cherry")
except KeyError as e:
    print("get('cherry') raised KeyError:", e)


# ---------------------------------------------------------------------------
# Seeing a collision happen
# ---------------------------------------------------------------------------
# With only 8 buckets, it doesn't take many keys before two of them
# land in the same bucket by coincidence. When that happens, chaining
# is what keeps both entries intact instead of one overwriting the other.
demo_table = HashTable(size=4)   # small on purpose, to force a collision

for word in ["one", "two", "three", "four", "five"]:
    demo_table.set(word, len(word))

print("\ndemo_table buckets (small size forces collisions):")
for i, bucket in enumerate(demo_table.buckets):
    print(f"  bucket {i}: {bucket}")
# Any bucket holding more than one [key, value] pair is a collision --
# both keys hashed to the same index, and chaining stored them side by
# side instead of losing one.


# ---------------------------------------------------------------------------
# Why this matters for complexity
# ---------------------------------------------------------------------------
# get(), set(), and remove() are all O(1) on AVERAGE, because in the
# typical case each bucket holds zero or one item, so "search the
# bucket" is nearly instant. But if the hash function is bad, or the
# table has too few buckets for how many keys it holds, MANY keys can
# collide into the same bucket -- and searching a long chain inside one
# bucket degrades toward O(n), the same cost as searching a plain list.
#
# This is exactly the caveat built_in_complexities.py flagged for
# Python's real dict: "O(1) average," not "O(1) always." Now you've
# seen the mechanism that makes both the average case fast and the
# worst case possible.


# ---------------------------------------------------------------------------
# Try it yourself
# ---------------------------------------------------------------------------
# 1. Create a HashTable(size=2) and add 6 different keys to it. Print
#    the buckets and count how many keys ended up sharing a bucket.
# 2. Modify _hash() to always `return 0` (every key goes to the same
#    bucket). Confirm the hash table still works correctly -- then
#    time inserting and looking up 10,000 keys with this broken hash
#    function versus the real one, to feel the O(n) worst case for
#    yourself.
# 3. Compare this file's set()/get()/remove() against Python's real
#    dict methods in Data_Structures/dictionaries.py -- same behavior,
#    but now you've seen what's happening underneath.