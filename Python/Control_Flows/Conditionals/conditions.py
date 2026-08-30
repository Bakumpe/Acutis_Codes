# Acutis_Codes/Python/Control_Flows/Conditionals/conditions.py
"""
    A conditional tests a single specific condition and runs code only when
    that condition is True. It uses the same if/elif/else syntax as
    branching.py, but the emphasis is different:

        - branching.py:  "which one of these several paths applies?"
        - conditions.py: "does this one specific thing hold true or not?"

    Usage:
        if condition:
            # code block
        elif another_condition:
            # code block
        else:
            # code block

    Use Cases:
        1. Guarding code so it only runs when a precondition is met
           (e.g. only divide if the divisor isn't zero).
        2. Validating input before acting on it.
        3. Short-circuiting logic with `and` / `or` to avoid unnecessary or
           unsafe work (e.g. `x != 0 and 10 / x > 1`).
"""

# 1. A single condition with no else - if it's False, nothing happens
x = 10
if x > 5:
    print("x is greater than 5")

# 2. A single condition with an else - exactly two outcomes
y = 20
if y % 2 == 0:
    print("y is even")
else:
    print("y is odd")

# 3. Guarding against an unsafe operation with `and` (short-circuit
#    evaluation) - Python only evaluates the second half of the condition if
#    the first half is True, so this is safe even when divisor is 0.
divisor = 0
if divisor != 0 and (100 / divisor) > 1:
    print("100 / divisor is greater than 1")
else:
    print("skipped the division - divisor is 0")

# 4. Validating input before using it
raw_input_value = "42"
if raw_input_value.isdigit():
    number = int(raw_input_value)
    print("Valid number:", number)
else:
    print("Invalid number:", raw_input_value)

print("y is", y)