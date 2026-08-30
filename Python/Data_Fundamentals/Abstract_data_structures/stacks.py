# Acutis_Codes/Python/Data_Fundamentals/Abstract_Data_Structures/stacks.py

"""
STACKS

A stack is not a separate Python type -- it's a set of RULES layered on
top of a regular list (or deque), restricting how you're allowed to add
and remove items. Python's real built-in collection types are list,
tuple, dict, and set; a stack is one way of *using* those types.

A stack follows LIFO -- Last In, First Out. Whatever gets added most
recently is the first thing to come back out, just like a stack of
plates: you take the top plate off first, and you add new plates to
the top too.

    [ 3 ]  <- top: add/remove here
    [ 2 ]
    [ 1 ]  <- bottom

This file shows two ways to build one:
    1. A plain list, using .append() and .pop()
    2. collections.deque, an alternative with the same big-O behavior
"""


# ---------------------------------------------------------------------------
# 1. Stack using a plain list
# ---------------------------------------------------------------------------
my_stack = []

my_stack.append(1)
my_stack.append("Hello")
my_stack.append(3)
print("stack after 3 appends:", my_stack)

last_out = my_stack.pop()   # removes and returns the TOP element (the end of the list)
print("removed:", last_out)
print("stack after pop():", my_stack)

# Why this is a stack and not a queue: we always add with .append() (to
# the end) and always remove with .pop() (also from the end -- no index
# given). The moment you removed with .pop(0) instead, you'd have a
# queue, not a stack -- the RULES are what define the structure, not
# the list itself. Compare this file with queues.py side by side.


# ---------------------------------------------------------------------------
# Why a list works well for a stack (unlike for a queue)
# ---------------------------------------------------------------------------
# Both .append() and .pop() (with no argument) operate on the END of
# the list, and Python lists are built so that adding/removing from the
# end is O(1) -- no shifting of other elements required.
#
# This is the opposite situation from queues.py, where .pop(0) removes
# from the FRONT and forces an O(n) shift of every remaining element.
# A stack never touches the front, so a plain list is genuinely fine
# to use here -- you don't need deque for correctness or performance.


# ---------------------------------------------------------------------------
# 2. Stack using collections.deque (a common alternative)
# ---------------------------------------------------------------------------
from collections import deque

# deque works equally well as a stack: .append() and .pop() (no
# argument) both operate on the same end, same as with a list. Some
# style guides prefer deque for stacks anyway, purely for consistency
# with queue code -- functionally, for a stack, it makes no real
# difference versus a plain list.

my_deque_stack = deque()

my_deque_stack.append(1)
my_deque_stack.append("Hello")
my_deque_stack.append(3)
print("\ndeque stack after 3 appends:", my_deque_stack, "| type:", type(my_deque_stack))

last_out = my_deque_stack.pop()
print("removed:", last_out)
print("deque stack after pop():", my_deque_stack)


# ---------------------------------------------------------------------------
# Peeking and checking for empty
# ---------------------------------------------------------------------------
# "Peeking" means looking at the top item WITHOUT removing it -- useful
# when you want to know what's next without committing to processing it yet.
if my_deque_stack:
    print("\npeek (top item):", my_deque_stack[-1])

# An empty stack (or list) is falsy, so you can check emptiness directly
# in an if-statement instead of writing len(my_deque_stack) == 0.
empty_stack = []
print("is empty_stack empty?", not empty_stack)


# ---------------------------------------------------------------------------
# Try it yourself
# ---------------------------------------------------------------------------
# 1. Add five items to a stack, then pop them off one at a time,
#    printing the stack after each pop. Confirm the order you get
#    items back is the REVERSE of the order you added them -- that's
#    the "last in, first out" behavior in action.
# 2. Call .pop() on an empty list or deque and read the error Python
#    raises (IndexError). Real stack implementations usually check
#    "is it empty?" before popping, to avoid crashing on this exact case.
# 3. This is the exact structure DFS uses to decide which node to
#    visit next (or Python's own call stack does it for you, if you
#    write DFS recursively) -- see Algorithms/DFS/dfs.py, and compare
#    its traversal order against BFS's in Algorithms/BFS/bfs.py.