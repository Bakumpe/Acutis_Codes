# Acutis_Codes/Python/Control_Flows/Branching/branching.py
"""
    Branching is a control flow mechanism that lets a program follow one of
    several possible paths depending on a condition, using if / elif / else.

    Usage:
        if condition:
            # code block
        elif another_condition:
            # code block
        else:
            # code block

    Example:
        x = 10
        if x > 5:
            print("x is greater than 5")
        elif x == 5:
            print("x is equal to 5")
        else:
            print("x is less than 5")

    Use Cases:
        1. Executing different code blocks based on a condition.
        2. Making decisions based on user input or other runtime factors.
        3. Handling different scenarios, such as error handling or input validation.
        4. Combining multiple conditions with logical operators (and, or, not)
           to express more complex decision logic.
        5. Breaking complex logic into smaller, readable, maintainable branches.

    Note - Branching vs. Conditionals:
        "Branching" and "conditionals" both describe if/elif/else in Python, and
        the terms are often used interchangeably. This repo splits them by
        emphasis: branching.py focuses on choosing between multiple mutually
        exclusive PATHS (ranges, categories), while conditions.py in
        ../Conditionals/ focuses on testing a single specific condition.
"""

# 1. Basic if / elif / else - three mutually exclusive branches
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# 2. Branching with a single logical condition
y = 20
if y > 10 and y < 30:
    print("y is between 10 and 30")

# 3. Chained comparison - Python lets you write the above more naturally
if 10 < y < 30:
    print("y is between 10 and 30 (chained comparison)")

# 4. Nested branching - a branch inside another branch
age = 20
has_id = True
if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("Entry denied: no ID")
else:
    print("Entry denied: underage")

# 5. Flattening the nested version into a single elif chain - usually
#    preferred, since flat code is generally easier to read than nested code
#    when the logic allows it
if age >= 18 and has_id:
    print("Entry allowed (flat version)")
elif age >= 18 and not has_id:
    print("Entry denied: no ID (flat version)")
else:
    print("Entry denied: underage (flat version)")