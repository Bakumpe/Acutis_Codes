# Dynamic Programming

> **Where this fits:** this is the hands-on counterpart to
> [Section 15 — Recursion](../../../../README.md#15-recursion) in the main
> cross-language reference. Read that section first if you haven't — DP is
> best understood as "recursion, plus a memory for what you've already
> solved." Code here lives alongside [`BFS/`](../BFS/bfs.py) and
> [`DFS/`](../DFS/dfs.py) in the `Algorithms/` folder, and follows the same
> Python-only convention (this topic is about the *technique*, not a
> language comparison).

## What is Dynamic Programming?

Dynamic Programming (DP) is a technique for solving problems by breaking them
down into smaller subproblems, solving each subproblem only once, and reusing
those results instead of recomputing them.

DP is not an algorithm itself — it's a *strategy*. Memoization and tabulation
are the two ways you actually implement that strategy in code.

```
Dynamic Programming (the idea)
        |
        +--> Memoization   (top-down, recursive, cached)
        |
        +--> Tabulation    (bottom-up, iterative, tabled)
```

Both approaches solve the exact same problem and produce the exact same
answer — they just build the solution in opposite directions.

---

## When does a problem qualify for DP?

A problem is a good candidate for Dynamic Programming when it has **both**
of these properties:

### 1. Optimal Substructure
The solution to the overall problem can be constructed from solutions to
smaller versions of the same problem.

> Example: `fib(n) = fib(n-1) + fib(n-2)` — the answer for `n` depends
> directly on answers for smaller inputs.

### 2. Overlapping Subproblems
Solving the problem the naive (plain recursive) way causes the *same*
smaller subproblem to be solved over and over again.

> Example: computing `fib(5)` the naive way calls `fib(3)` twice,
> `fib(2)` three times, and so on — wasted, repeated work.

If a problem has optimal substructure but subproblems **don't** overlap
(e.g., classic divide-and-conquer like merge sort), DP doesn't help —
plain recursion is already efficient.

---

## Approach 0: Brute-Force Recursion (the starting point)

Before memoizing anything, write the naive recursive version. It's the
same shape you'll keep for Approach 1 — you're about to add exactly one
thing to it.

```python
def fib(n):
    if n <= 1:                       # base case
        return n
    return fib(n - 1) + fib(n - 2)   # recursive case — but recomputes work!

print(fib(10))  # 55
```

This is O(2^n) — every call branches into two more, and the same smaller
values get recomputed over and over. That's the overlapping-subproblems
symptom from above, and it's the signal to reach for DP.

---

## Approach 1: Memoization (Top-Down)

**Idea:** Start from the original problem and recurse *downward* into
smaller subproblems, the same way you naturally think through the problem.
Before solving a subproblem, check if it's already been solved — if so,
reuse the cached answer instead of recomputing it.

**Characteristics:**
- Built directly on top of the recursive solution above — only one change
- Uses a cache (dict or array) to store results
- Only computes subproblems that are actually needed
- Uses the call stack, so very deep recursion can risk a stack overflow
  (Python's default recursion limit is ~1000 calls)

**Fibonacci — Memoized (manual cache):**
```python
cache = {}

def fib(n):
    if n <= 1:
        return n
    if n in cache:            # already solved -> reuse
        return cache[n]
    cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n]

print(fib(50))  # 12586269025 — instant, vs. unusable with brute force
```

**Fibonacci — Memoized (Python's built-in decorator):**
Python's standard library gives you memoization for free — worth knowing,
even though writing it manually (above) is what builds the intuition.
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(50))  # 12586269025
```

**How to think through it out loud (interview framing):**
> "I'll write the brute-force recursive version first to nail the logic.
> Then I'll check: are the same subproblems being solved more than once?
> If yes, I'll add a cache so each unique subproblem is only computed once."

---

## Approach 2: Tabulation (Bottom-Up)

**Idea:** Start from the *smallest* subproblems and build upward, filling
a table (usually a list) iteratively, until you reach the original
problem's answer.

**Characteristics:**
- Built with a loop, not recursion
- No call stack risk — safe for very large inputs
- Typically computes every subproblem from the smallest up to `n`,
  even ones that might not strictly be needed
- Often easier to optimize for space (you frequently only need the
  last one or two entries of the table, not the whole thing)

**Fibonacci — Tabulated:**
```python
def fib(n):
    if n <= 1:
        return n
    table = [0] * (n + 1)
    table[0], table[1] = 0, 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]

print(fib(50))  # 12586269025
```

**Space-optimized version** (since we only ever need the last two values):
```python
def fib(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

print(fib(50))  # 12586269025
```

---

## Side-by-Side Comparison

| | Memoization (Top-Down) | Tabulation (Bottom-Up) |
|---|---|---|
| Direction | Big problem → small subproblems | Small subproblems → big problem |
| Implementation | Recursion + cache | Loop + table (list) |
| Computes | Only subproblems actually needed | Usually all subproblems up to `n` |
| Risk | Stack overflow on deep recursion | None — purely iterative |
| Space | Cache + call stack | Table (often optimizable to O(1)) |
| Feels like | "Solve the natural recursive way, but remember answers" | "Build up the answer step by step" |
| Time Complexity | O(n) for Fibonacci | O(n) for Fibonacci |

Both versions above run in **O(n) time** and compute the **exact same
values** — they're just approaching the same set of subproblem answers
from opposite directions.

---

## A Practical Workflow for Coding Challenges

When you're given a problem in an interview or challenge, walk through it
in this order:

1. **Write the brute-force recursive solution first.**
   Focus purely on getting the recursive relationship correct — don't
   worry about efficiency yet. (This is Approach 0 above.)

2. **Identify overlapping subproblems.**
   Ask: "Am I solving the same smaller input more than once?" If the
   brute-force recursion tree has repeated branches, DP applies.

3. **Add memoization.**
   Wrap the recursive calls with a cache check. This is usually the
   fastest way to go from brute-force to efficient, since it's a small
   change to code you already wrote.

4. **Convert to tabulation if needed.**
   If you're worried about recursion depth on large inputs, or want to
   squeeze out extra space savings, rewrite the memoized version as an
   iterative bottom-up table.

**Say this out loud in an interview:**
> "This problem has optimal substructure and overlapping subproblems, so
> it's a Dynamic Programming problem. I'll start with memoization since
> it's a direct extension of the recursive brute-force solution, then
> convert to tabulation if I need to avoid recursion overhead or reduce
> memory usage."

---

## Common DP Problems to Practice

Use these to practice recognizing DP and applying both approaches:

- Climbing Stairs (count ways to reach step `n`)
- Coin Change (fewest coins to make an amount)
- Longest Common Subsequence (LCS)
- 0/1 Knapsack
- Longest Increasing Subsequence
- Edit Distance
- House Robber (max sum with no two adjacent elements)

For each one, try solving it three ways in order: **brute-force recursion
→ memoization → tabulation.** Doing all three builds the intuition for
recognizing DP problems quickly and choosing the right implementation
under time pressure.

---

> **Next step:** once this clicks, revisit [`BFS/bfs.py`](../BFS/bfs.py) and
> [`DFS/dfs.py`](../DFS/dfs.py) with DP in mind — several graph problems
> (shortest path counting, longest path in a DAG) are traversal *plus* a
> memo table bolted on, which is exactly this pattern applied to a
> different kind of subproblem.