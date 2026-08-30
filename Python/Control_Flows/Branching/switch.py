# Acutis_Codes/Python/Control_Flows/Branching/switch.py
"""
    Python has no dedicated switch/case keyword - it gained one, spelled
    match/case, only in Python 3.10. Before 3.10, and still today in many
    codebases, a "switch" is emulated with either a dictionary dispatch or a
    plain if/elif chain. This file shows all three approaches on the same
    problem so you can compare them directly.

    Problem: given a day number (1-7), return the day's name.

    Use Cases:
        1. Dispatching on a fixed, known set of values (menu choices, HTTP
           methods, command names) without writing a long if/elif chain.
        2. Mapping input values directly to functions to call
           (dictionary dispatch).
        3. Using match/case (3.10+) for structural pattern matching -
           matching not just a value, but a value's shape (tuples, lists,
           objects, wildcards).
"""

import sys

# 1. if/elif/else - works on every Python version, but grows long fast
def day_name_if_elif(day: int) -> str:
    if day == 1:
        return "Monday"
    elif day == 2:
        return "Tuesday"
    elif day == 3:
        return "Wednesday"
    elif day == 4:
        return "Thursday"
    elif day == 5:
        return "Friday"
    elif day == 6:
        return "Saturday"
    elif day == 7:
        return "Sunday"
    else:
        return "Invalid day"


# 2. Dictionary dispatch - the classic "Python switch statement". A dict
#    lookup is O(1) average (see Data_Fundamentals/Algorithm_Analysis/
#    built_in_complexities.py), so this also scales better than a long
#    elif chain as the number of cases grows.
DAY_NAMES = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}

def day_name_dict(day: int) -> str:
    return DAY_NAMES.get(day, "Invalid day")


# 3. match/case (Python 3.10+) - Python's real switch statement. Unlike a
#    plain dict lookup, it can also match on shape/structure, not just a
#    single value (not shown here, but worth exploring separately).
def day_name_match(day: int) -> str:
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6 | 7:
            # `|` means "match either value" - here, either weekend day
            return "Saturday or Sunday (weekend)"
        case _:
            # `_` is the wildcard - it matches anything not caught above
            return "Invalid day"


if __name__ == "__main__":
    for d in (1, 5, 7, 99):
        print(f"day {d}: if/elif -> {day_name_if_elif(d)}")
        print(f"day {d}: dict     -> {day_name_dict(d)}")
        if sys.version_info >= (3, 10):
            print(f"day {d}: match    -> {day_name_match(d)}")
        else:
            print(f"day {d}: match    -> skipped (requires Python 3.10+)")
        print("-" * 40)