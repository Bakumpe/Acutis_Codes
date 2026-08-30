# Acutis_Codes/Python/Data_Fundamentals/Algorithm_Analysis/big_o_notation.py

"""
BIG-O NOTATION

Big-O describes how the COST of an operation grows as the size of its
input (usually called n) grows. It's not a stopwatch measurement --
it's a way to talk about the *shape* of the growth, so you can compare
two approaches without needing to run them both first.

"Cost" usually means time, but the same notation is used for space
(memory) too -- this file focuses on time.

Common complexities, from best to worst, roughly in the order you'll
meet them:

    O(1)        constant     -- cost doesn't change as n grows
    O(log n)    logarithmic  -- cost grows slowly; doubling n adds
                                one more step, not double the steps
    O(n)        linear       -- cost grows directly with n
    O(n log n)  linearithmic -- slightly worse than linear; typical
                                of good sorting algorithms
    O(n^2)      quadratic    -- cost grows with the SQUARE of n;
                                typical of nested loops over the
                                same data
    O(2^n)      exponential  -- cost doubles with every additional
                                item; explodes fast, avoid when
                                possible

We only care about what happens as n gets LARGE. Constants and
lower-order terms get dropped: an algorithm that does "3n + 100" steps
is still just O(n), because as n grows toward infinity, the "+100" and
the "3" stop mattering compared to the effect of n itself.
"""


# ---------------------------------------------------------------------------
# O(1) -- constant time
# ---------------------------------------------------------------------------
# The cost is the same whether the list has 3 items or 3 million.
def get_first_item(items):
    return items[-1]   # always exactly one step, regardless of len(items)


small_list = [10, 20, 30]
large_list = list(range(1_000_000))

print("get_first_item(small_list):", get_first_item(small_list))
print("get_first_item(large_list):", get_first_item(large_list))
# Both calls above do the same amount of work. That's what O(1) means.


# ---------------------------------------------------------------------------
# O(n) -- linear time
# ---------------------------------------------------------------------------
# The cost grows directly with the size of the input. Double the list,
# double the work.
def contains_value(items, target):
    for item in items:          # in the worst case, checks every item once
        if item == target:
            return True
    return False


print("\ncontains_value(small_list, 20):", contains_value(small_list, 20))
print("contains_value(small_list, 99):", contains_value(small_list, 99))
# Searching a 3-item list and a 3-million-item list for a value that
# ISN'T there takes proportionally longer on the bigger list -- that
# proportional relationship is exactly what O(n) describes. This is
# also why queues.py flagged list.pop(0) as O(n): removing the front
# item forces every remaining item to shift over by one, which is one
# unit of work per remaining item.


# ---------------------------------------------------------------------------
# O(n^2) -- quadratic time
# ---------------------------------------------------------------------------
# A loop inside a loop, both running over the same data. This is the
# classic shape of "compare every item to every other item."
def has_duplicate_pair(items):
    for i in range(len(items)):
        for j in range(len(items)):
            if i != j and items[i] == items[j]:
                return True
    return False


print("\nhas_duplicate_pair([1, 2, 3]):", has_duplicate_pair([1, 2, 3]))
print("has_duplicate_pair([1, 2, 2]):", has_duplicate_pair([1, 2, 2]))
# For a list of 10 items, this does roughly 10 * 10 = 100 comparisons.
# For a list of 1,000 items, that's roughly 1,000 * 1,000 = 1,000,000
# comparisons. The work grows much faster than the input does -- that's
# the hallmark of O(n^2), and why nested loops over the same data are
# usually the first thing to look at when code runs slower than expected.


# ---------------------------------------------------------------------------
# O(log n) -- logarithmic time
# ---------------------------------------------------------------------------
# Each step eliminates HALF of the remaining possibilities, instead of
# checking one item at a time. Binary search is the textbook example --
# it only works on a SORTED list, because it relies on being able to
# rule out half the list based on a single comparison.
def binary_search(sorted_items, target):
    low, high = 0, len(sorted_items) - 1
    steps = 0
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if sorted_items[mid] == target:
            print(f"found {target} in {steps} step(s)")
            return mid
        elif sorted_items[mid] < target:
            low = mid + 1       # target must be in the right half
        else:
            high = mid - 1      # target must be in the left half
    print(f"{target} not found, after {steps} step(s)")
    return -1


sorted_numbers = list(range(0, 1_000_000, 2))   # 500,000 sorted even numbers
binary_search(sorted_numbers, 999_998)
binary_search(sorted_numbers, 999_999)   # not in the list -- it's odd
# Even searching half a million items, binary search takes around 19-20
# steps at most, because each step cuts the search space in half:
# 500,000 -> 250,000 -> 125,000 -> ... down to 1. That halving pattern
# is exactly what "logarithmic" means: log2(500,000) is approximately 19.


# ---------------------------------------------------------------------------
# Comparing growth side by side
# ---------------------------------------------------------------------------
# This doesn't measure real time -- it just prints how many "steps"
# each complexity class implies for the same values of n, so you can
# see the shapes diverge.
import math

print("\n{:>10} {:>8} {:>10} {:>10} {:>12} {:>15}".format(
    "n", "O(1)", "O(log n)", "O(n)", "O(n log n)", "O(n^2)"
))
for n in (10, 100, 1_000, 10_000):
    o1 = 1
    o_log_n = round(math.log2(n))
    o_n = n
    o_n_log_n = round(n * math.log2(n))
    o_n2 = n ** 2
    print("{:>10} {:>8} {:>10} {:>10} {:>12} {:>15}".format(
        n, o1, o_log_n, o_n, o_n_log_n, o_n2
    ))
# Notice O(n^2) pulls away from the others almost immediately, while
# O(log n) barely grows at all even as n grows by 1000x.


# ---------------------------------------------------------------------------
# Try it yourself
# ---------------------------------------------------------------------------
# 1. Add an O(n^2) row to the comparison table above (n ** 2) and an
#    O(2^n) row (2 ** n) for small values of n only (try n up to 20 --
#    anything larger will take a very long time or overflow your
#    patience). Watch how fast O(2^n) outgrows everything else.
# 2. Go back to Abstract_Data_Structures/queues.py and stacks.py.
#    Explain out loud (or in a comment) why list.append() is O(1) but
#    list.pop(0) is O(n), using the ideas from this file.
# 3. Look at BFS and DFS in Algorithms/ -- both visit every node and
#    every edge once, which makes them O(V + E) (V = number of nodes,
#    E = number of edges). Find the loop in each file that visits
#    neighbors and confirm this for yourself.