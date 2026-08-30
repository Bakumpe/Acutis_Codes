# Control_Flows

Part of the **Acutis_Codes** project — a public collection of Python fundamentals, data structures, and algorithms, written to help people learn Python from the ground up. Contributions, corrections, and additions are welcome.

This folder covers how a Python program *decides what to do next*: choosing between paths (branching/conditionals) and repeating work (loops), plus the underlying distinction between a statement and an expression that both of those are built on.

**Prerequisite:** this folder assumes you already know Python's basic types and operators. See [`../Data_Fundamentals/README.md`](../Data_Fundamentals/README.md) — specifically its *Variables & DataTypes*, *Type Systems*, and *Operators* sections — before starting here.

## Requirements

- Python 3.7 or later for everything except `switch.py`'s `match/case` examples, which require **Python 3.10+** (those examples are skipped gracefully on older versions, not an error).
- No third-party packages — everything here uses the Python standard library only.

## How to run

Every file in this folder is a standalone, runnable script. Clone the repo, navigate into the folder that interests you, and run the file directly:

```bash
git clone https://github.com/<your-username>/Acutis_Codes.git
cd Acutis_Codes/Python/Control_Flows/Branching
python branching.py
```

Each script prints its own output to the terminal, so you can read the code alongside what it actually produces. Nothing here writes to disk, so — unlike `Data_Fundamentals/File_Handling` — there's no generated `demo/` folder to worry about.

## Folder structure

```
Control_Flows/
├── Branching/
│   ├── branching.py
│   └── switch.py
├── Conditionals/
│   └── conditions.py
├── Loops/
│   ├── for.py
│   └── while.py
└── Statements_vs_Expressions/
    └── statements_vs_expressions.py
```

## Suggested learning order

```
Statements vs. Expressions → Conditionals → Branching → Loops (for → while)
```

Each stage below builds on the one before it.

### 1. Statements vs. Expressions (`Statements_vs_Expressions/statements_vs_expressions.py`)

Before writing if-statements and loops, it helps to know what a "statement" actually is, versus an "expression" — because every branch and loop condition you write from here on is an expression, and every branch and loop itself is a statement. This file lays out the distinction directly, then shows the walrus operator (`:=`, Python 3.8+) as a case that deliberately blurs the line: it's an assignment that's *also* usable as an expression.

**Learn it by:** going through each line and asking "does this produce a value I could print, or does it just do something?" Then try replacing the walrus-operator example with a plain `=` assignment and see why it no longer fits inside the `if (...)`.

### 2. Conditionals (`Conditionals/conditions.py`)

The `if` / `elif` / `else` syntax, applied to testing one specific condition at a time — "is this true or not?" — including short-circuit evaluation (`and`/`or` skipping unnecessary or unsafe work) and basic input validation.

**Learn it by:** predicting the output of each conditional before running the file, especially the short-circuit example (`divisor != 0 and ...`) — trace through why it's safe even when `divisor` is `0`.

### 3. Branching (`Branching/branching.py`, `Branching/switch.py`)

The same `if` / `elif` / `else` syntax as conditionals, but applied to choosing between several mutually exclusive *paths* rather than testing one thing. `branching.py` also covers nested branches and when to flatten them into a single `elif` chain. `switch.py` covers the closest Python equivalent of a switch/case statement — Python has no `switch` keyword — comparing three approaches on the same problem: an `if/elif` chain, dictionary dispatch, and `match/case` (Python 3.10+).

**Learn it by:** rewriting the nested `if` example in `branching.py` as a flat `elif` chain yourself before looking at the file's own flattened version. Then, in `switch.py`, add an 8th "day" case to all three implementations and notice which one required touching the least code.

### 4. Loops — for & while (`Loops/for.py`, `Loops/while.py`)

Loops repeat a block of code. `for.py` covers iterating over a *known* sequence (`range()`, lists, `enumerate()`), including `break` and `continue`. `while.py` covers repeating *until a condition changes* — including Python's `while True` + `break` pattern for "run at least once" logic, since Python has no dedicated `do-while` keyword, and the lesser-known `while/else` construct.

**Learn it by:** running `for.py` and predicting each block's output before it prints, then doing the same for `while.py`. Pay close attention to the do-while pattern and the `while/else` example — both behave in ways beginners often get wrong on a first guess.

---

## How the pieces connect

```
statements_vs_expressions.py → the vocabulary: what a condition IS
                                (an expression) vs. what a branch/loop IS
                                (a statement)
conditions.py                → testing ONE condition with if/elif/else
branching.py                 → choosing between MULTIPLE paths with the
                                same syntax, plus nested vs. flat branching
switch.py                    → the same "choose one of many paths" problem,
                                solved 3 different ways (if/elif, dict, match)
for.py / while.py            → repeating a block of code — over a known
                                sequence (for) or until a condition changes
                                (while)
```

Conditionals and branching answer "which code runs?"; loops answer "how many times does it run?" Together they're the two ways a Python program's execution can deviate from running top-to-bottom, one line at a time — which is why everything past this point in the wider Acutis_Codes project (file handling, data structure traversal, BFS/DFS, and beyond) leans on both constantly.

## Contributing

This project is public so others can learn Python alongside these files. If you're contributing:

- Keep each file focused on one concept.
- Include runnable examples with `print()` output, not just definitions.
- Add comments explaining *why* something works, not just *what* it does — the goal is teaching, not just showing correct code.
- If you add a new concept, update this README with where it fits in the learning order.
- Name new folders `Like_This` (underscores, no spaces) to stay consistent with the rest of the repo and avoid `%20`-encoding issues in URLs and scripts.

Pull requests, issue reports, and beginner questions are all welcome.