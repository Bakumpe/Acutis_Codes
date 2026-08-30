# Acutis_Codes/Python/Data_Fundamentals/File_Handling/a.py

"""
"a" -- APPEND MODE

- Creates the file if it doesn't exist yet (same as "w" in that regard).
- If the file already exists, new writes are added to the END --
  unlike "w", it does NOT erase what's already there first.

This file appends into demo/a.txt. Unlike w.py and r.py, this script
is DESIGNED to change behavior across multiple runs -- run it several
times in a row and watch the file grow each time, since "a" never
resets it for you.
"""

import os

DEMO_DIR = os.path.join(os.path.dirname(__file__), "demo")
DEMO_FILE = os.path.join(DEMO_DIR, "a.txt")

os.makedirs(DEMO_DIR, exist_ok=True)


# ---------------------------------------------------------------------------
# Appending with "a"
# ---------------------------------------------------------------------------
with open(DEMO_FILE, "a") as f:
    f.write("this line was appended by a run of a.py\n")

print("appended a line to demo/a.txt")


# ---------------------------------------------------------------------------
# Reading it back to see the growth
# ---------------------------------------------------------------------------
with open(DEMO_FILE, "r") as f:
    contents = f.read()

print("\ncurrent contents of demo/a.txt:")
print(contents)
print(f"({contents.count(chr(10))} lines so far -- run this script again to add one more)")


# ---------------------------------------------------------------------------
# Compare: appending several lines in one run with .writelines()
# ---------------------------------------------------------------------------
more_lines = ["extra line A\n", "extra line B\n"]

with open(DEMO_FILE, "a") as f:
    f.writelines(more_lines)

with open(DEMO_FILE, "r") as f:
    print("\nafter appending two more lines with writelines():")
    print(f.read())


# ---------------------------------------------------------------------------
# Try it yourself
# ---------------------------------------------------------------------------
# 1. Run this script five times in a row without deleting demo/a.txt.
#    Confirm the file keeps growing by 3 lines per run, forever --
#    "a" has no concept of "start over."
# 2. Delete demo/a.txt manually (or add an os.remove(DEMO_FILE) call
#    at the top, guarded by "if os.path.exists(...)") to reset the
#    demo back to empty.
# 3. Compare this file to w.py -- both can create a missing file, but
#    only "w" resets an existing one.