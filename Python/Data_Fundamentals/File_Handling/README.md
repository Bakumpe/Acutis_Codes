# File_Handling

A quick reference for the file object returned by `open()` — what each method does, and which of `r.py` / `w.py` / `a.py` / `x.py` / `b.py` demonstrates it.

## What `f` actually is

```python
with open("demo.txt", "r") as f:
    ...
```

`f` isn't a keyword — it's just a variable name holding the **file object** that `open()` returns. That object represents an open connection to the file on disk, and it keeps track of *where you currently are* in the file (often called the cursor, or file pointer). Every read or write call below moves that cursor forward.

## The methods

| Call | What it does | Needs mode |
|---|---|---|
| `f.read()` | Reads the entire remaining contents as one string (or `bytes` in binary mode). | read (`"r"`, `"rb"`) |
| `f.readline()` | Reads just the next line, including its trailing `\n`. Call it again and you get the *following* line — the cursor remembers where it left off. | read |
| `f.readlines()` | Reads all remaining lines at once, returned as a list of strings, each still ending in `\n`. | read |
| `for line in f:` | Iterates the file one line at a time, without loading the whole thing into memory first. The most memory-efficient way to process a large file. | read |
| `f.write(text)` | Writes `text` (a `str` in text mode, `bytes` in binary mode) to the file at the current cursor position. Does **not** add a newline for you. | write (`"w"`, `"a"`, `"x"`, or with `"b"`) |
| `f.writelines(list_of_strings)` | Writes multiple strings one after another. Like `.write()`, it does **not** insert `\n` between them — your strings need to already include line breaks if you want separate lines. | write |
| `f.close()` | Closes the connection to the file, flushing any unwritten data to disk and releasing the OS-level file handle. | any |

## Why `f.close()` is rarely called directly

Every script in this folder uses `with open(...) as f:` instead of calling `open()`/`close()` manually:

```python
# what we use
with open("demo.txt", "r") as f:
    contents = f.read()

# what this replaces
f = open("demo.txt", "r")
contents = f.read()
f.close()   # easy to forget — especially if an error happens before this line
```

`with` is a **context manager**: the moment the indented block ends — whether it finishes normally or an exception is raised partway through — Python calls `f.close()` for you automatically. Skipping `with` and forgetting `.close()` can leave a file locked from other programs, or leave written data sitting in a buffer that never actually reaches disk.

## Read methods vs. write methods — don't mix them up

A file object only supports the operations its mode allows:

- Open with `"r"` and call `f.write(...)` → `io.UnsupportedOperation: not writable`
- Open with `"w"` and call `f.read()` → `io.UnsupportedOperation: not readable`

This is intentional, not a limitation to work around — it forces you to be explicit about whether a piece of code is reading or writing.

## Where each method shows up in this folder

| Method | File(s) |
|---|---|
| `f.read()` | `r.py`, `w.py`, `a.py`, `x.py`, `b.py` |
| `f.readline()` | `r.py` |
| `f.readlines()` | `r.py` |
| `for line in f:` | `r.py` |
| `f.write()` | `w.py`, `a.py`, `x.py`, `b.py` |
| `f.writelines()` | `w.py`, `a.py` |
| `f.close()` (implicit, via `with`) | every file |

## Try it yourself

1. Open a file in `"r"` mode and try calling `f.write("test")` on it. Read the `io.UnsupportedOperation` error and confirm it matches the "don't mix them up" section above.
2. In `r.py`, replace the `for line in f:` loop with `f.readlines()` followed by a regular `for` loop over the resulting list. Confirm the printed output is identical — they're two ways of getting to the same place, but one loads everything into memory first and one doesn't.
3. Remove the `with` keyword from one example in `w.py` and manage `open()`/`close()` yourself instead. Deliberately raise an error between the two calls (e.g. reference an undefined variable) and confirm `.close()` never runs — this is the exact failure mode `with` exists to prevent.