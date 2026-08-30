# Acutis_Codes/Python/Data_Fundamentals/File_Handling/x.py

"""
"x" -- EXCLUSIVE CREATE MODE

- Creates the file ONLY if it doesn't already exist.
- If the file already exists, it raises FileExistsError instead of
  touching it -- the opposite failure case from "r".

This is useful whenever overwriting an existing file would be a
mistake (e.g. saving a user's export, generating a report) and you
want Python to refuse rather than silently clobber something.

This file targets demo/x.txt. The FIRST time you run this script, it
creates the file successfully. Every run AFTER that raises
FileExistsError, because the file is already there.
"""

import os

DEMO_DIR = os.path.join(os.path.dirname(__file__), "demo")
DEMO_FILE = os.path.join(DEMO_DIR, "x.txt")

os.makedirs(DEMO_DIR, exist_ok=True)


# ---------------------------------------------------------------------------
# Attempting an exclusive create
# ---------------------------------------------------------------------------
try:
    with open(DEMO_FILE, "x") as f:
        f.write("created by the first run of x.py\n")
    print("created demo/x.txt for the first time")
except FileExistsError as e:
    print("FileExistsError caught -- demo/x.txt already exists:", e)
    print("this is expected on every run after the first")


# ---------------------------------------------------------------------------
# Reading whatever is there now, regardless of which branch ran
# ---------------------------------------------------------------------------
with open(DEMO_FILE, "r") as f:
    print("\ncurrent contents of demo/x.txt:")
    print(f.read())


# ---------------------------------------------------------------------------
# Try it yourself
# ---------------------------------------------------------------------------
# 1. Run this script twice in a row and confirm you get the success
#    message once, then the FileExistsError message every time after.
# 2. Delete demo/x.txt manually and rerun -- confirm it succeeds again.
# 3. Compare the error you get here (FileExistsError) to the one r.py
#    demonstrates (FileNotFoundError) -- "x" and "r" fail in exactly
#    opposite situations.