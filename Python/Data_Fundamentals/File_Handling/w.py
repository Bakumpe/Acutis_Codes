# Acutis_Codes/Python/Data_Fundamentals/File_Handling/w.py

"""
"w" -- WRITE MODE

- Creates the file if it doesn't exist yet.
- ERASES the file first if it already exists, then writes fresh.
- If you only want to add to what's already there, see a.py instead.

This file writes into demo/w.txt, in a "demo" subfolder next to this
script. open() creates missing FILES for you, but it does NOT create
missing FOLDERS -- that's what os.makedirs(..., exist_ok=True) is for
below. exist_ok=True means "don't error if the folder is already there."
"""

import os

DEMO_DIR = os.path.join(os.path.dirname(__file__), "demo")
DEMO_FILE = os.path.join(DEMO_DIR, "w.txt")

os.makedirs(DEMO_DIR, exist_ok=True)


# ---------------------------------------------------------------------------
# Writing with "w"
# ---------------------------------------------------------------------------
# "with" is a context manager -- it automatically closes the file for
# you when the indented block ends, even if an error happens inside
# it. Always prefer "with" over calling open()/close() manually.
with open(DEMO_FILE, "w") as f:
    f.write("line one\n")
    f.write("line two\n")

print("wrote demo/w.txt")

with open(DEMO_FILE, "r") as f:
    print(f.read())


# ---------------------------------------------------------------------------
# Proof that "w" erases first
# ---------------------------------------------------------------------------
# Run this script twice in a row -- demo/w.txt still only ever has the
# two lines below, never four, because every run wipes the file clean
# before writing again.
with open(DEMO_FILE, "w") as f:
    f.write("this run's line one\n")
    f.write("this run's line two\n")

with open(DEMO_FILE, "r") as f:
    print("after rewriting with 'w':")
    print(f.read())


# ---------------------------------------------------------------------------
# Writing multiple lines at once with .writelines()
# ---------------------------------------------------------------------------
lines_to_write = ["fruit\n", "vegetable\n", "grain\n"]

with open(DEMO_FILE, "w") as f:
    f.writelines(lines_to_write)

with open(DEMO_FILE, "r") as f:
    print("after writelines():")
    print(f.read())
# .writelines() does NOT add "\n" for you -- if the strings in your
# list don't already end in "\n", everything runs together on one
# line. Try removing the "\n" from lines_to_write above and rerunning
# to see it happen.


# ---------------------------------------------------------------------------
# Try it yourself
# ---------------------------------------------------------------------------
# 1. Run this script twice in a row and open demo/w.txt in between --
#    confirm it never grows past what a single run writes.
# 2. Remove the "\n" characters from lines_to_write and rerun. Look at
#    demo/w.txt and see all three words squashed onto one line.
# 3. Compare this file to a.py, which uses the SAME open() call shape
#    but never erases what's already there.