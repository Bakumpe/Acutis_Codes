# Acutis_Codes/Python/Control_Flows/Loops/while.py
"""
    A while loop repeats a block of code as long as a condition stays True.
    Unlike a for loop (which iterates a known sequence), a while loop is best
    when you don't know in advance how many times you'll need to loop.

    Usage:
        while condition:
            # code block

    Example:
        x = 0
        while x < 5:
            print(x)
            x += 1

    Use Cases:
        1. Repeating code until a condition is met (unknown iteration count).
        2. Waiting for a user input or external event.
        3. Building a "run at least once" loop with `while True` + `break`
           (Python has no dedicated do-while keyword - see example 2 below).
        4. Building a controlled infinite loop (e.g. a game loop or server loop).

    Incrementing / decrementing:
        You control a while loop's exit condition manually - forgetting to
        update the loop variable (e.g. `x += 1`) causes an infinite loop.
"""

# 1. Basic while loop - runs while x < 5
x = 0
while x < 5:
    print("Iteration:", x)
    x += 1

print("-" * 20)

# 2. "Do-while" equivalent - Python has no do-while keyword, so this pattern
#    (while True + a break at the end) is the standard way to guarantee the
#    body runs at least once before the condition is ever checked.
x = 0
while True:
    print("Iteration:", x)
    x += 1
    if x >= 5:
        break

print("-" * 20)

# 3. while/else - the else block runs only if the loop finished WITHOUT
#    hitting a break. Useful for "search and report if not found" logic.
target = 99
numbers = [1, 2, 3, 4, 5]
i = 0
while i < len(numbers):
    if numbers[i] == target:
        print(f"Found {target}")
        break
    i += 1
else:
    print(f"{target} was not found in the list")

# 4. continue in a while loop - skip the rest of this iteration, the
#    condition is still checked on the next pass
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue  # skip even counts
    print("Odd count:", count)