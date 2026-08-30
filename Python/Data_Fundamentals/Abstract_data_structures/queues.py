# Acutis_Codes/Python/Data_Fundamentals/Abstract_Data_Structures/queues.py

"""
QUEUES

A queue is not a separate Python type -- it's a set of RULES layered on
top of a regular list (or deque), restricting how you're allowed to add
and remove items. Python's real built-in collection types are list,
tuple, dict, and set; a queue is one way of *using* those types.

A queue follows FIFO -- First In, First Out. Whatever gets added first
is the first thing to come back out, just like a checkout line: the
first person to join the line is the first person served.

    add here ->  [ 1 ][ 2 ][ 3 ]  -> removed from here
                 (back)      (front)

This file shows two ways to build one:
    1. A plain list, using .append() and .pop(0)
    2. collections.deque, which is the version you should actually use
"""


# ---------------------------------------------------------------------------
# 1. Queue using a plain list
# ---------------------------------------------------------------------------
my_queue = []

my_queue.append(1)
my_queue.append("Hello")
my_queue.append(3)
print("queue after 3 appends:", my_queue)

first_out = my_queue.pop(0)   # removes and returns the FRONT element (index 0)
print("removed:", first_out)
print("queue after pop(0):", my_queue)

# Why this is a queue and not a stack: we always add with .append() (to
# the back) and always remove with .pop(0) (from the front). The moment
# you removed with .pop() instead of .pop(0), you'd have a stack, not a
# queue -- the RULES are what define the structure, not the list itself.


# ---------------------------------------------------------------------------
# Why a list is a poor choice for a real queue
# ---------------------------------------------------------------------------
# list.pop(0) is an O(n) operation: Python has to shift every remaining
# element one position to the left to fill the gap at index 0. For a
# short queue like the one above, that's invisible. For a queue with
# thousands of items being added and removed constantly, all that
# shifting adds up and slows your program down.
#
# list.append() is fine either way -- it's O(1), adding to the *end*
# of a list never requires shifting anything.


# ---------------------------------------------------------------------------
# 2. Queue using collections.deque (the correct tool for the job)
# ---------------------------------------------------------------------------
from collections import deque

# "deque" (pronounced "deck") stands for double-ended queue: a
# structure built to add and remove from BOTH ends efficiently.
# Internally it isn't a flat array like a list -- it's implemented so
# that both .append() and .popleft() run in O(1) time, no shifting
# required, no matter how large the queue gets.

my_deque_queue = deque()

my_deque_queue.append(1)
my_deque_queue.append("Hello")
my_deque_queue.append(3)
print("\ndeque after 3 appends:", my_deque_queue, "| type:", type(my_deque_queue))

first_out = my_deque_queue.popleft()   # removes and returns the front element
print("removed:", first_out)
print("deque after popleft():", my_deque_queue)


# ---------------------------------------------------------------------------
# Peeking and checking for empty
# ---------------------------------------------------------------------------
# "Peeking" means looking at the front item WITHOUT removing it -- useful
# when you want to know what's next without committing to processing it yet.
if my_deque_queue:
    print("\npeek (front item):", my_deque_queue[0])

# An empty deque (or list) is falsy, so you can check emptiness directly
# in an if-statement instead of writing len(my_deque_queue) == 0.
empty_queue = deque()
print("is empty_queue empty?", not empty_queue)


# ---------------------------------------------------------------------------
# Try it yourself
# ---------------------------------------------------------------------------
# 1. Add five items to a deque, then pop them off one at a time with
#    popleft(), printing the queue after each pop. Confirm the order
#    you get items back matches the order you added them.
# 2. Try my_deque_queue.appendleft(0) -- what end does that add to?
#    Look up deque's four core operations: append, appendleft, pop,
#    popleft -- notice a deque can act as BOTH a queue and a stack
#    depending on which pair of methods you use.
# 3. This is the exact structure BFS uses to decide which node to
#    visit next -- see Algorithms/BFS/bfs.py, and notice the queue
#    there is built with deque for the same efficiency reason covered
#    above.