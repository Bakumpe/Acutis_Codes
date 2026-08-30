# Acutis_Codes/Python/Data_Fundamentals/File_Handling/r.py

"""
"r" -- READ MODE (the default if you don't pass a mode at all)

- The file MUST already exist -- "r" never creates one for you.
- Opening a missing file with "r" raises FileNotFoundError.

This file reads from demo/r.txt. The setup block below writes that
file first using "w", purely so this script is self-contained and
runnable on a fresh clone -- the actual topic of this file is
everything AFTER the setup block: the different ways to read.
"""

import os

DEMO_DIR = os.path.join(os.path.dirname(__file__), "demo")
DEMO_FILE = os.path.join(DEMO_DIR, "r.txt")

os.makedirs(DEMO_DIR, exist_ok=True)

# --- setup only, not the focus of this file (see w.py for "w" itself) ---
with open(DEMO_FILE, "w") as f:
    f.write("line one\n")
    f.write("line two\n")
    f.write("line three\n")
# --- end setup ---


# ---------------------------------------------------------------------------
# Reading the whole file at once with .read()
# ---------------------------------------------------------------------------
with open(DEMO_FILE, "r") as f:
    contents = f.read()   # one big string, including the \n newlines

print(".read() result:")
print(repr(contents))   # repr() shows the \n characters instead of acting on them


# ---------------------------------------------------------------------------
# Reading one line at a time with .readline()
# ---------------------------------------------------------------------------
with open(DEMO_FILE, "r") as f:
    first_line = f.readline()    # reads just ONE line, including its \n
    second_line = f.readline()   # the file remembers where it left off

print("\n.readline() first call:", repr(first_line))
print(".readline() second call:", repr(second_line))


# ---------------------------------------------------------------------------
# Reading every line into a list with .readlines()
# ---------------------------------------------------------------------------
with open(DEMO_FILE, "r") as f:
    all_lines = f.readlines()   # a LIST of every line, each still ending in \n

print("\n.readlines() result:", all_lines)


# ---------------------------------------------------------------------------
# Iterating line by line (the most common, most memory-efficient way)
# ---------------------------------------------------------------------------
# .read() and .readlines() both load the ENTIRE file into memory at
# once. For a small file that's harmless, but for a huge file (think
# gigabytes of logs) it can eat all your RAM. Iterating directly reads
# one line at a time instead.
print("\niterating line by line:")
with open(DEMO_FILE, "r") as f:
    for line in f:
        print("  ->", line.strip())   # .strip() removes the trailing \n


# ---------------------------------------------------------------------------
# What happens when the file doesn't exist
# ---------------------------------------------------------------------------
try:
    with open(os.path.join(DEMO_DIR, "this_file_does_not_exist.txt"), "r") as f:
        f.read()
except FileNotFoundError as e:
    print("\nFileNotFoundError caught:", e)


# ---------------------------------------------------------------------------
# Try it yourself
# ---------------------------------------------------------------------------
# 1. Add a fourth f.write(...) line to the setup block, rerun, and
#    predict what .readlines() will return before printing it.
# 2. Call f.readline() three times in a row inside one "with" block on
#    a 3-line file, then call it a FOURTH time. What do you get back
#    when there's nothing left to read?
# 3. Replace "r" with "rb" in the main .read() example and look at
#    what comes back -- compare it to b.py, which covers binary mode
#    properly.