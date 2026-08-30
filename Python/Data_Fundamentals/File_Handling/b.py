# Acutis_Codes/Python/Data_Fundamentals/File_Handling/b.py

"""
"b" -- BINARY MODE

"b" isn't used alone -- it's added onto another mode: "wb" (write
binary), "rb" (read binary), "ab" (append binary), and so on. It tells
Python to treat the file as raw BYTES instead of text.

Why this matters:
    - Text mode ("r"/"w") expects a string and handles text encoding
      (e.g. converting between Python's internal representation and
      UTF-8 on disk) and newline translation for you automatically.
    - Binary mode expects a `bytes` object, does NO encoding and NO
      newline translation, and hands you back the exact raw bytes on
      read. This is required for non-text files -- images, audio,
      zip files -- where "translating newlines" would corrupt the data.

This file writes and reads demo/b.bin.
"""

import os

DEMO_DIR = os.path.join(os.path.dirname(__file__), "demo")
DEMO_FILE = os.path.join(DEMO_DIR, "b.bin")

os.makedirs(DEMO_DIR, exist_ok=True)


# ---------------------------------------------------------------------------
# Writing bytes with "wb"
# ---------------------------------------------------------------------------
# You can't write a plain str in binary mode -- it has to be a bytes
# object. .encode() converts a str into bytes using a given encoding
# (utf-8 is the standard default).
text_part = "Hello".encode("utf-8")
raw_bytes = bytes([0, 1, 2, 255])   # bytes don't have to represent text at all

with open(DEMO_FILE, "wb") as f:
    f.write(text_part)
    f.write(raw_bytes)

print("wrote demo/b.bin")


# ---------------------------------------------------------------------------
# Reading it back with "rb"
# ---------------------------------------------------------------------------
with open(DEMO_FILE, "rb") as f:
    contents = f.read()

print("\nraw bytes read back:", contents)
print("type:", type(contents))   # bytes, not str

# The first 5 bytes came from a real piece of text, so they CAN be
# decoded back into a string:
decoded_text = contents[:5].decode("utf-8")
print("first 5 bytes decoded as text:", decoded_text)

# The remaining bytes are NOT valid text -- trying to .decode() them
# would raise a UnicodeDecodeError, because they were never text to
# begin with. This is exactly why binary mode exists: not everything
# on disk is meant to be interpreted as characters.
print("remaining raw bytes (not text):", list(contents[5:]))


# ---------------------------------------------------------------------------
# Why text mode would break on this same data
# ---------------------------------------------------------------------------
# Uncomment to see it fail -- opening arbitrary binary data in text
# mode can raise a UnicodeDecodeError, because Python tries (and
# fails) to interpret every byte as part of a text encoding:
#
# with open(DEMO_FILE, "r") as f:
#     f.read()   # UnicodeDecodeError, most likely


# ---------------------------------------------------------------------------
# Try it yourself
# ---------------------------------------------------------------------------
# 1. Uncomment the text-mode read above and read the traceback --
#    identify which byte value it chokes on.
# 2. Change raw_bytes to bytes(range(256)) (every possible byte value)
#    and confirm .read() in "rb" mode still gets all 256 values back
#    correctly, byte for byte.
# 3. Compare "wb"/"rb" here to "w"/"r" in w.py and r.py -- notice the
#    open() calls look almost identical; only the mode string and the
#    type you write/read (bytes vs str) actually change.