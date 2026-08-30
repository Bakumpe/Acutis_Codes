# Acutis_Codes/Python/Control_Flows/Loops/for.py
"""
    A for loop iterates over a sequence of values - a range, list, tuple,
    string, dict, or any other iterable - running its code block once per
    item.

    Usage:
        for variable in sequence:
            # code block

    Example:
        for i in range(5):
            print(i)

    Use Cases:
        1. Iterating over a sequence of values, such as a list, tuple, or string.
        2. Running a block of code a fixed number of times (range()).
        3. Iterating over a collection while also tracking position (enumerate()).
        4. Skipping items with `continue` or stopping early with `break`.

    range() step:
        range(start, stop, step) controls how the loop counter moves each
        iteration - see example 2 below.
"""

# 1. Basic for loop over range() - runs exactly 5 times, i = 0..4
for i in range(5):
    print("Iteration:", i)

# 2. range() with start, stop, and step - counting down by 2
for i in range(10, 0, -2):
    print("Countdown:", i)

# 3. For loop over a list
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print("Item:", item)

# 4. enumerate() - get both the index and the value while iterating
for index, item in enumerate(my_list):
    print(f"Index {index}: {item}")

# 5. continue - skip the rest of this iteration, keep looping
for item in my_list:
    if item % 2 == 0:
        continue  # skip even numbers
    print("Odd item:", item)

# 6. break - stop the loop entirely once a condition is met
for item in my_list:
    if item == 4:
        print("Found 4, stopping loop")
        break
    print("Checked:", item)

# 7. Nested for loop - a loop inside a loop, useful for grids and tables
for row in range(3):
    for col in range(3):
        print(f"({row}, {col})", end="  ")
    print()  # newline after each row