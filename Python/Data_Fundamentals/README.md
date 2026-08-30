# Data_Fundamentals

Part of the **Acutis_Codes** project — a public collection of Python fundamentals, data structures, and algorithms, written to help people learn Python from the ground up. Contributions, corrections, and additions are welcome.

This folder covers the building blocks every programmer needs before tackling harder problems (like the ones under `Python/LeetCode/`): variables and types, core data structures, operators, abstract data structures, and two foundational algorithms.

> **Related folder:** decision-making and repetition (`if`/`elif`/`else`, loops) are covered separately in [`../Control_Flows/README.md`](../Control_Flows/README.md). That folder only needs *Variables & DataTypes*, *Type Systems*, and *Operators* from here, so it's safe to read it right after step 3 below and before continuing on to *File Handling*.

## Requirements

- Python 3.7 or later (the examples rely on f-strings and guaranteed dict insertion order, both introduced in 3.6/3.7).
- No third-party packages — everything here uses the Python standard library only.

## How to run

Every file in this folder is a standalone, runnable script. Clone the repo, navigate into the folder that interests you, and run the file directly:

```bash
git clone https://github.com/Bakumpe/Acutis_Codes.git
cd Acutis_Codes/Python/Data_Fundamentals/Variables_&_DataTypes
python datatypes.py
```

Each script prints its own output to the terminal, so you can read the code alongside what it actually produces. There's nothing to import or install — just run the file.

## Folder structure

```
Data_Fundamentals/
├── Variables_&_DataTypes/
│   └── datatypes.py
├── Type_Systems/
│   └── typesSystem.py
├── Operators/
│   ├── operators.py
│   └── tenary.py
├── File_Handling/
│   ├── r.py
│   ├── w.py
│   ├── a.py
│   ├── x.py
│   ├── b.py
│   └── demo/            <- generated automatically when you run any script above
├── Data_Structures/
│   ├── lists.py
│   ├── tuples.py
│   ├── dictionaries.py
│   └── sets.py
├── Algorithm_Analysis/
│   ├── big_o_notation.py
│   └── built_in_complexities.py
├── Abstract_Data_Structures/
│   ├── stacks.py
│   ├── queues.py
│   └── hash_table.py
└── Algorithms/
    ├── BFS/
    │   └── bfs.py
    └── DFS/
        └── dfs.py
```

## Suggested learning order

Concepts here build on each other. Going out of order will work, but you'll hit gaps — for example, you can't understand a stack without knowing what a list is, and you can't understand BFS without knowing what a queue is. Follow this path:

1. **Variables & DataTypes** — what data looks like in Python
2. **Type Systems** — how Python decides what kind of data you're holding, and why it matters
3. **Operators** — how you act on and compare that data
4. **File Handling** — how you save data to disk and load it back, using the strings and control flow you already know
5. **Data Structures** — how you group many pieces of data together
6. **Algorithm Analysis** — how to describe and compare the cost of an operation, once you have real data structures to point at
7. **Abstract Data Structures** — structures built *on top of* the ones above, with rules about how data goes in and comes out
8. **Algorithms** — step-by-step procedures that use the structures above to solve real problems


```
Variables & Types → Operators → File Handling → Data Structures → Algorithm Analysis → Abstract Data Structures → Algorithms
```

Each stage is the vocabulary the next stage assumes you already have.

> **Where Control_Flows fits:** step 4 (*File Handling*) already talks about "the strings and control flow you already know" — that control flow (if/else, loops) is exactly what lives in [`../Control_Flows/`](../Control_Flows/README.md). If you haven't covered branching and loops yet, this is the natural point to detour there before continuing to File Handling.

---

## 1. Variables & DataTypes (`Variables_&_DataTypes/datatypes.py`)

Every program starts with data: numbers, text, true/false values. This file covers Python's built-in primitive types — `int`, `float`, `str`, `bool` — and how to store them in variables.

**Learn it by:** creating a few variables of each type, printing their values, and using `type(x)` to confirm what Python thinks each one is. Try converting between types (`int("5")`, `str(5)`, `float("3.14")`) and notice what breaks (`int("hello")`).

## 2. Type Systems (`Type_Systems/typesSystem.py`)

Once you know the types exist, this covers *how* Python handles them: Python is **dynamically typed** (a variable's type is decided at runtime, and can change) and **strongly typed** (it won't silently convert `"5" + 5` for you — that raises an error). This is the "why" behind quirks you'll hit constantly, like why `"5" + "5"` gives `"55"` but `5 + 5` gives `10`.

**Learn it by:** deliberately writing code that mixes types (e.g. `"5" + 5`) and reading the error Python gives you. Compare that to a statically typed language if you've used one — the difference is the whole point.

## 3. Operators (`Operators/operators.py`, `Operators/tenary.py`)

Operators are how you act on variables: arithmetic (`+ - * / // % **`), comparison (`== != < > <= >=`), logical (`and or not`), and assignment (`= += -=`). `tenary.py` covers the ternary conditional expression — `x if condition else y` — a compact one-line if/else.

**Learn it by:** writing small expressions and predicting the output *before* running them, especially around operator precedence and the difference between `/` (float division) and `//` (integer division). Rewrite a few `if/else` blocks as ternary expressions to see when they help readability and when they hurt it.

## 4. File Handling (`File_Handling/r.py`, `w.py`, `a.py`, `x.py`, `b.py`)

Everything covered above lives only in memory — the moment your program ends, it's gone. File handling is how a program saves data to disk (writing) and loads it back later (reading), using `open(filename, mode)`. Each mode gets its own file here, since each one has a genuinely different failure case and behavior:

| File | Mode | Behavior |
|---|---|---|
| `r.py` | `"r"` | File must already exist — errors with `FileNotFoundError` if not |
| `w.py` | `"w"` | Creates the file if missing, **erases** it first if it exists |
| `a.py` | `"a"` | Creates the file if missing, **adds to the end** if it exists |
| `x.py` | `"x"` | Creates the file only if it does **not** already exist — errors with `FileExistsError` if it does |
| `b.py` | `"b"` (combined with the above, e.g. `"rb"`/`"wb"`) | Reads/writes raw `bytes` instead of text — no encoding, no newline translation |

Every script writes into its own file inside a `demo/` subfolder (`demo/r.txt`, `demo/w.txt`, etc.), which each script creates automatically with `os.makedirs(..., exist_ok=True)` — `open()` creates missing *files* but never missing *folders*, so this step is required. `demo/` isn't checked into the repo; it's generated the first time you run any of these scripts, so feel free to delete it and rerun at any time.

All five only depend on strings and basic control flow, both already covered above — file handling doesn't need any of the data structures or algorithms that come later. It's placed here because it's a genuinely standalone skill, though you'll often see it combined with later topics (e.g. reading a file's lines directly into a list).

**Learn it by:** running `w.py` first and predicting `demo/w.txt`'s contents before printing them, then `r.py` to see the read-side equivalents. Run `a.py` two or three times in a row without deleting `demo/a.txt` and watch it grow — this is the one file in the set that's *designed* to behave differently across runs. Then run `x.py` twice and compare its `FileExistsError` to `r.py`'s `FileNotFoundError` — they're opposite failure modes. Finish with `b.py` and note how little the code shape changes between text and binary mode, even though the underlying behavior is quite different.

## 5. Data Structures (`Data_Structures/`)

These are the four built-in containers you'll use in almost every Python program:

| Structure | Ordered? | Mutable? | Duplicates? | Typical use |
|---|---|---|---|---|
| `lists.py` | Yes | Yes | Yes | A general-purpose, changeable sequence |
| `tuples.py` | Yes | No | Yes | A fixed sequence that shouldn't change (e.g. coordinates) |
| `dictionaries.py` | Yes (insertion order, 3.7+) | Yes | Keys: no. Values: yes | Fast lookups by key (`name → value`) |
| `sets.py` | No | Yes | No | Fast membership checks, removing duplicates |

**Learn it by:** taking the same real-world data (say, a list of students and their grades) and representing it as each of the four structures. Notice what gets easier and what gets harder each time — that's the actual lesson. For example: a `dict` makes "look up Alice's grade" instant; a `list` makes you search for it.

## 6. Algorithm Analysis (`Algorithm_Analysis/big_o_notation.py`, `built_in_complexities.py`)

Once you can compare data structures ("a dict lookup feels faster than searching a list"), you need a formal way to talk about *why*. `big_o_notation.py` covers what `O(1)` (constant), `O(log n)` (logarithmic), `O(n)` (linear), `O(n log n)` (linearithmic), `O(n²)` (quadratic), and `O(2ⁿ)` (exponential) actually mean.

`built_in_complexities.py` then applies that vocabulary to the methods you already use every day — `.append()`, `.pop()`, `.pop(0)`, `.sort()`, `in`, string concatenation, and their `dict`/`set` equivalents — so you know which everyday calls are cheap and which quietly get expensive as your data grows.

This isn't a new data structure or algorithm — it's the vocabulary you need to *evaluate* every structure and algorithm that comes after it. It's also the "why" behind claims made elsewhere in this repo, like `queues.py` noting that `list.pop(0)` is `O(n)` while `deque.popleft()` is `O(1)`.

**Learn it by:** running the growth-comparison table in `big_o_notation.py` and watching how fast `O(n²)` pulls away from `O(n)` as `n` grows. Then work through `built_in_complexities.py` and, for each method shown, predict its complexity before reading the answer. Finally, go back to `queues.py` and `stacks.py` and explain, in your own words, why each operation used there has the complexity it has.

## 7. Abstract Data Structures (`Abstract_Data_Structures/stacks.py`, `queues.py`, `hash_table.py`)

A **stack** and a **queue** aren't new Python types — they're *rules* layered on top of a list, restricting how you're allowed to add and remove items:

- **Stack (LIFO — last in, first out):** you can only add/remove from one end (the "top"). Think of a stack of plates.
- **Queue (FIFO — first in, first out):** you add at one end and remove from the other. Think of a checkout line.

This distinction matters a lot once you reach `Algorithms/`: **DFS uses a stack, BFS uses a queue** — same idea, different structure underneath, and that single difference is what changes their whole behavior.

`hash_table.py` follows the same "build it from a list" pattern, but for a different goal: instead of controlling *order*, it builds a lookup mechanism that mimics what Python's built-in `dict` and `set` already do internally. It implements a hash function, a bucket array, and collision handling (chaining), so you can see exactly why `built_in_complexities.py` describes dict/set operations as "O(1) average" rather than "O(1) always."

**Learn it by:** implementing stacks and queues using nothing but a plain Python `list` (`.append()`/`.pop()` for a stack; `.append()`/`.pop(0)` or `collections.deque` for a queue). Push a sequence of items into each and pop them back out — watch the order come out reversed for the stack and preserved for the queue. Then work through `hash_table.py`, force a collision with a small bucket count, and confirm chaining keeps both keys intact.

## 8. Algorithms — BFS & DFS (`Algorithms/BFS/bfs.py`, `Algorithms/DFS/dfs.py`)

Both are strategies for visiting every node in a graph (or tree) — the difference is what they visit next:

- **BFS (Breadth-First Search):** explores level by level, using a **queue**. Visits a node, then *all* of its direct neighbors, before going further out. Good for finding the shortest path in an unweighted graph.
- **DFS (Depth-First Search):** explores as deep as possible down one path before backtracking, using a **stack** (or recursion, which uses the call stack automatically). Good for exploring every possibility, maze-solving, and cycle detection.

This is the payoff of everything above: BFS and DFS are just "traverse a graph" `+` "the abstract data structure from step 7" `+` "the dict/list from step 5 used to represent the graph itself." You genuinely cannot understand *why* they behave differently without already understanding stacks vs. queues.

**Learn it by:** running both on the same small graph and printing the visited order for each. Trace it by hand first — write down what's in the stack/queue after every step — then compare your trace to the actual printed output. If they don't match, that mismatch is exactly where your understanding has a gap.

---

## How the pieces connect

```
datatypes.py + typesSystem.py   → the raw material (numbers, strings, booleans)
operators.py + tenary.py        → how you manipulate that material
r.py / w.py / a.py / x.py / b.py → how you save that material to disk
                                   and load it back, one mode at a time
lists / tuples / dicts / sets   → how you group that material together
big_o_notation.py               → the vocabulary for comparing how costly
                                   any operation on the structures above is
built_in_complexities.py        → that vocabulary applied to the exact
                                   list/dict/set/str methods used everywhere
                                   else in this repo
stacks.py / queues.py           → rules for how you add/remove from a list
hash_table.py                   → the mechanism behind dict/set's
                                   O(1) average lookup, built from a list
bfs.py / dfs.py                 → traversal algorithms that need a graph
                                   (usually stored as a dict) + a queue or stack
```

Nothing here is standalone — each file is a dependency for something later in the folder. If a concept in `Algorithms/` feels confusing, the fix is almost always to go back one or two steps, not to push forward.

## Contributing

This project is public so others can learn Python alongside these files. If you're contributing:

- Keep each file focused on one concept.
- Include runnable examples with `print()` output, not just definitions.
- Add comments explaining *why* something works, not just *what* it does — the goal is teaching, not just showing correct code.
- If you add a new concept, update this README with where it fits in the learning order.
- Name new folders `Like_This` (underscores, no spaces) to stay consistent with the rest of the repo and avoid `%20`-encoding issues in URLs and scripts.
- If your file generates output on disk at runtime (like `File_Handling/demo/`), add that folder to `.gitignore` rather than committing generated files.

Pull requests, issue reports, and beginner questions are all welcome.