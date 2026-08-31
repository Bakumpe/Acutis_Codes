# Programming Fundamentals: A Cross-Language Reference

Every general-purpose language — Python, JavaScript, Go, C++, Ruby, whatever
comes next — is built from the same small set of ideas. Syntax changes.
These don't. Learn them once, deeply, and picking up a new language becomes
mostly a matter of learning new *spelling* for concepts you already
understand.

This guide walks through each core concept, explains what it *means*
(not just how to type it), and shows it in both **Python** and
**JavaScript** side by side so you can see where the languages agree and
where they diverge.

**This edition is ordered as a learning path**, not just a topic index —
work through the phases in order. Each phase builds on the one before it,
and a few concepts (type systems, memory, error-as-value) are deliberately
placed *after* you've written enough code to feel the problems they solve,
rather than upfront where they'd just be abstract.

> **How this file relates to the rest of the repo:** this is the
> conceptual reference for **Acutis_Codes** — it explains *why* each idea
> exists and compares it across languages, but it's meant to be read
> alongside runnable code, not instead of it. Where a section has a
> hands-on, Python-only counterpart elsewhere in this repo, you'll see a
> **Related code in this repo** callout pointing to it, e.g.
> [`Python/Data_Fundamentals/`](Python/Data_Fundamentals/README.md) and
> [`Python/Control_Flows/`](Python/Control_Flows/README.md). Sections
> without a callout don't have a dedicated folder yet — that's an open
> spot for a contribution (see [Contributing](#contributing) at the
> bottom).

---

## Table of Contents

**Phase 1 — The Absolute Basics**
1. [Variables & Data Types](#1-variables--data-types)
2. [Operators](#2-operators)
3. [Statements vs. Expressions](#3-statements-vs-expressions)
4. [Conditionals](#4-conditionals)
5. [Loops](#5-loops)
6. [Branching: break, continue, return](#6-branching-break-continue-return)

**Phase 2 — Organizing Code**
7. [Functions](#7-functions)
8. [Scope & Lifetime](#8-scope--lifetime)
9. [Data Structures](#9-data-structures)
10. [Procedural Programming](#10-procedural-programming)

**Phase 3 — Robust, Connected Programs**
11. [Input/Output](#11-inputoutput)
12. [Exceptions (try/catch)](#12-exceptions-trycatch)
13. [Modules & Packages](#13-modules--packages)
14. [APIs & Libraries](#14-apis--libraries)

**Phase 4 — Deeper Concepts**
15. [Recursion](#15-recursion)
16. [Type Systems](#16-type-systems)
17. [Pointers & References](#17-pointers--references)
18. [Memory Management](#18-memory-management)

**Phase 5 — Paradigms & Advanced Patterns**
19. [Object-Oriented Programming](#19-object-oriented-programming)
20. [Functional Programming](#20-functional-programming)
21. [Error-as-Value](#21-error-as-value)

[How to Use This Reference](#how-to-use-this-reference)
[Contributing](#contributing)

---

# Phase 1 — The Absolute Basics

*Goal: be able to write a simple, working program — no functions yet,
just values, decisions, and repetition.*

## 1. Variables & Data Types

A variable is a named reference to a value in memory. Every language has
some core primitive types: numbers, text (strings), booleans (true/false),
and a concept of "nothing" (`None` / `null`).

**Python**
```python
age = 25            # int
price = 19.99        # float
name = "Alice"       # str
is_active = True     # bool
nothing = None        # NoneType
```

**JavaScript**
```javascript
let age = 25;              // number (JS has one numeric type)
let price = 19.99;         // number
let name = "Alice";        // string
let isActive = true;       // boolean
let nothing = null;        // null
let notDefined;            // undefined — JS's second "nothing"
```

**Key difference:** JavaScript distinguishes `null` (intentionally
"nothing") from `undefined` (never assigned) — Python only has `None`.

**Apply it when:** always — this is the atomic unit of every program.
Choosing the right type up front (e.g., a number vs. a string that looks
like a number) avoids a huge class of bugs.

> **Related code in this repo:** [`Python/Data_Fundamentals/Variables_&_DataTypes/datatypes.py`](Python/Data_Fundamentals/Variables_&_DataTypes/datatypes.py)

---

## 2. Operators

Arithmetic (`+ - * / %`), comparison (`== != < > <= >=`), logical
(`and/or/not` or `&& || !`), and assignment (`= += -=`) operators are
universal, but their exact behavior varies.

**Python**
```python
7 // 2   # 3   — floor (integer) division
7 % 2    # 1   — remainder
2 ** 10  # 1024 — exponentiation
5 == 5.0 # True — value equality
```

**JavaScript**
```javascript
Math.floor(7 / 2); // 3 — JS has no // operator, use Math.floor
7 % 2;              // 1
2 ** 10;             // 1024
5 == 5;              // true — loose equality (coerces types)
5 === 5;             // true — strict equality (no coercion, preferred)
"5" == 5;             // true  (loose — coerces!)
"5" === 5;            // false (strict — no coercion)
```

**Apply it when:** always prefer `===`/`!==` in JavaScript over `==`/`!=`
to avoid coercion surprises. In Python, `==` is already strict about type
in the way JS's `===` is.

> **Related code in this repo:** [`Python/Data_Fundamentals/Operators/operators.py`](Python/Data_Fundamentals/Operators/operators.py) and [`tenary.py`](Python/Data_Fundamentals/Operators/tenary.py)

---

## 3. Statements vs. Expressions

A **statement** performs an action and produces no value of its own
(`if`, a loop, an assignment). An **expression** evaluates *to* a value
and can be used anywhere a value is expected. Understanding the
difference explains why you can write `x = 5 + 3` (an expression on the
right) but not `x = if y: 1 else: 2` in most languages (though some, like
Python's ternary, blur this intentionally).

**Python**
```python
# expression — evaluates to a value
result = 5 + 3          # 8
is_adult = age >= 18    # True/False

# ternary expression (a compact if/else that evaluates to a value)
label = "adult" if age >= 18 else "minor"

# statement — performs an action, has no value
if age >= 18:
    print("Welcome")
```

**JavaScript**
```javascript
// expression
const result = 5 + 3;
const isAdult = age >= 18;

// ternary expression
const label = age >= 18 ? "adult" : "minor";

// statement
if (age >= 18) {
  console.log("Welcome");
}
```

**Apply it when:** you're deciding whether something can be assigned,
passed as an argument, or used inline — if it produces a value, it's an
expression and can go there; if not, it's a statement and needs its own
line.

> **Related code in this repo:** [`Python/Control_Flows/Statements_vs_Expressions/statements_vs_expressions.py`](Python/Control_Flows/Statements_vs_Expressions/statements_vs_expressions.py) — it also covers Python's walrus operator (`:=`), a rare case of an assignment that's *also* usable as an expression.

---

## 4. Conditionals

Conditionals let a program branch — run different code depending on
whether something is true or false.

**Python**
```python
age = 20

if age < 13:
    category = "child"
elif age < 20:
    category = "teen"
else:
    category = "adult"

# Python has no switch statement pre-3.10, but has match:
match category:
    case "child":
        print("Under 13")
    case "teen":
        print("Teenager")
    case _:
        print("Adult")
```

**JavaScript**
```javascript
const age = 20;
let category;

if (age < 13) {
  category = "child";
} else if (age < 20) {
  category = "teen";
} else {
  category = "adult";
}

switch (category) {
  case "child":
    console.log("Under 13");
    break;
  case "teen":
    console.log("Teenager");
    break;
  default:
    console.log("Adult");
}
```

**Apply it when:** the program needs to make a decision — validating
input, choosing which UI to render, handling different response codes
from an API.

> **Related code in this repo:** [`Python/Control_Flows/Conditionals/conditions.py`](Python/Control_Flows/Conditionals/conditions.py) and [`Python/Control_Flows/Branching/`](Python/Control_Flows/Branching/) (`branching.py` for if/elif/else paths, `switch.py` for `match`/dict-dispatch alternatives to a switch statement).

---

## 5. Loops

A loop repeats a block of code until some condition is no longer true.
The two universal shapes are: "repeat this a known number of times" (a
`for` loop) and "repeat this while a condition holds" (a `while` loop).

**Python**
```python
# for loop — iterate over a sequence
for i in range(5):
    print(i)  # 0 1 2 3 4

# while loop — repeat while a condition is true
count = 0
while count < 5:
    print(count)
    count += 1

# iterating directly over data (Python's preferred style)
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**JavaScript**
```javascript
// for loop
for (let i = 0; i < 5; i++) {
  console.log(i); // 0 1 2 3 4
}

// while loop
let count = 0;
while (count < 5) {
  console.log(count);
  count++;
}

// iterating directly over data
const fruits = ["apple", "banana", "cherry"];
for (const fruit of fruits) {
  console.log(fruit);
}

// or, functionally:
fruits.forEach(fruit => console.log(fruit));
```

**Apply it when:** you need to process every item in a collection, repeat
an action a fixed number of times, or keep retrying something until a
condition changes (polling, waiting for input, game loops).

> **Related code in this repo:** [`Python/Control_Flows/Loops/for.py`](Python/Control_Flows/Loops/for.py) and [`while.py`](Python/Control_Flows/Loops/while.py) — including `enumerate()`, `break`/`continue`, and Python's `while`/`else`, none of which have a direct JavaScript equivalent.

---

## 6. Branching: break, continue, return

These interrupt normal control flow: `break` exits a loop entirely,
`continue` skips to the next iteration, and `return` exits a function
(optionally handing back a value — you'll use `return` properly once you
hit Functions in Phase 2, but it belongs conceptually with `break`/
`continue` here).

**Python**
```python
for n in range(10):
    if n == 3:
        continue   # skip 3, keep looping
    if n == 7:
        break      # stop looping entirely
    print(n)

def first_even(numbers):
    for n in numbers:
        if n % 2 == 0:
            return n   # exits the function immediately
    return None
```

**JavaScript**
```javascript
for (let n = 0; n < 10; n++) {
  if (n === 3) continue; // skip 3
  if (n === 7) break;    // stop entirely
  console.log(n);
}

function firstEven(numbers) {
  for (const n of numbers) {
    if (n % 2 === 0) return n; // exits immediately
  }
  return null;
}
```

**Apply it when:** you want to stop early once you've found what you need
(search loops), skip irrelevant items without extra nesting, or exit a
function as soon as a result is known.

> **Related code in this repo:** `break` and `continue` are demonstrated directly inside [`Python/Control_Flows/Loops/for.py`](Python/Control_Flows/Loops/for.py) and [`while.py`](Python/Control_Flows/Loops/while.py) rather than in a separate file, since they only make sense in the context of a loop that's already running.

---

# Phase 2 — Organizing Code

*Goal: stop writing everything top-to-bottom in one block. Group logic
into reusable functions, and start working with real collections of
data instead of single values.*

## 7. Functions

A function is a named, reusable block of code that takes inputs
(parameters) and optionally produces an output (a return value). This is
the single most important tool for avoiding repeated code.

**Python**
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))              # Hello, Alice!
print(greet("Bob", "Hey"))         # Hey, Bob!

# anonymous (lambda) function
square = lambda x: x * x
```

**JavaScript**
```javascript
function greet(name, greeting = "Hello") {
  return `${greeting}, ${name}!`;
}

console.log(greet("Alice"));       // Hello, Alice!
console.log(greet("Bob", "Hey"));  // Hey, Bob!

// arrow function (JS's anonymous function)
const square = x => x * x;
```

**Apply it when:** you find yourself writing similar code more than
once — extract it into a function with parameters for the parts that
differ.

---

## 8. Scope & Lifetime

**Scope** determines *where* a variable is visible. **Lifetime**
determines *how long* it exists in memory. A variable declared inside a
function is typically local — it exists only while the function runs and
is invisible outside it.

**Python**
```python
x = "global"

def show():
    y = "local"       # only exists inside show()
    print(x)            # can read the global
    print(y)

show()
print(y)  # NameError — y doesn't exist out here
```

**JavaScript**
```javascript
let x = "global";

function show() {
  let y = "local"; // only exists inside show()
  console.log(x);   // can read the global
  console.log(y);
}

show();
console.log(y); // ReferenceError — y doesn't exist out here
```

**Closures** — a function "remembers" variables from the scope it was
created in, even after that outer scope has finished running:

```python
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter = make_counter()
print(counter())  # 1
print(counter())  # 2
```

```javascript
function makeCounter() {
  let count = 0;
  return function increment() {
    count += 1;
    return count;
  };
}

const counter = makeCounter();
console.log(counter()); // 1
console.log(counter()); // 2
```

**Apply it when:** you want to keep private state tied to a function
(like the counter above) without polluting the global scope — this
pattern underlies things like React hooks and event handler state.

---

## 9. Data Structures

The core containers almost every language provides in some form:

| Concept | Python | JavaScript |
|---|---|---|
| Ordered list | `list` — `[1, 2, 3]` | `Array` — `[1, 2, 3]` |
| Key-value map | `dict` — `{"a": 1}` | `Object` / `Map` |
| Unique collection | `set` — `{1, 2, 3}` | `Set` |
| Fixed, immutable sequence | `tuple` — `(1, 2)` | (no native tuple — use a frozen array or object) |

**Python**
```python
numbers = [1, 2, 3]
numbers.append(4)

person = {"name": "Alice", "age": 30}
print(person["name"])

unique = {1, 2, 2, 3}  # {1, 2, 3} — duplicates dropped

point = (10, 20)  # tuple — can't be modified after creation
```

**JavaScript**
```javascript
const numbers = [1, 2, 3];
numbers.push(4);

const person = { name: "Alice", age: 30 };
console.log(person.name);

const unique = new Set([1, 2, 2, 3]); // Set {1, 2, 3}

const point = Object.freeze([10, 20]); // closest JS equivalent to a tuple
```

> **Not a perfect match:** `Object.freeze()` is *shallow* — it stops the
> array's own elements from being reassigned, but if an element is itself
> an object or array, that nested value can still be mutated. Python's
> tuple has the same shallow-immutability caveat when it holds a mutable
> element like a list, so the two aren't as different as they first
> appear — neither one gives you deep immutability for free.

**Apply it when:** choosing a data structure is choosing performance
characteristics — use a map/dict for fast lookups by key, a set when you
only care about uniqueness/membership, a list/array when order matters.

> **Related code in this repo:** [`Python/Data_Fundamentals/Data_Structures/`](Python/Data_Fundamentals/Data_Structures/) (`lists.py`, `tuples.py`, `dictionaries.py`, `sets.py`) — and, for *why* one structure outperforms another, [`Algorithm_Analysis/built_in_complexities.py`](Python/Data_Fundamentals/Algorithm_Analysis/built_in_complexities.py).

---

## 10. Procedural Programming

The most straightforward paradigm: a sequence of instructions executed
top to bottom, organized into functions, without necessarily bundling
data and behavior together (as OOP does). Everything you've written up
to this point in the guide *is* procedural programming — it's worth
naming explicitly now that you have functions and data structures to
combine.

**Python**
```python
def calculate_total(prices, tax_rate):
    subtotal = sum(prices)
    tax = subtotal * tax_rate
    return subtotal + tax

prices = [10, 20, 30]
total = calculate_total(prices, 0.08)
print(f"Total: ${total:.2f}")
```

**JavaScript**
```javascript
function calculateTotal(prices, taxRate) {
  const subtotal = prices.reduce((sum, p) => sum + p, 0);
  const tax = subtotal * taxRate;
  return subtotal + tax;
}

const prices = [10, 20, 30];
const total = calculateTotal(prices, 0.08);
console.log(`Total: $${total.toFixed(2)}`);
```

**Apply it when:** the task is a straightforward sequence of steps —
scripts, small utilities, data processing pipelines — and doesn't need
the structure OOP or FP would add.

---

# Phase 3 — Robust, Connected Programs

*Goal: move past toy scripts. Read real input, talk to files and the
network, and stop letting one failure crash the whole program.*

## 11. Input/Output

Programs need to read data in (files, user input, network requests) and
send data out (console, files, network responses).

**Python**
```python
# console I/O
name = input("What's your name? ")
print(f"Hello, {name}")

# file I/O
with open("data.txt", "r") as f:
    contents = f.read()

with open("output.txt", "w") as f:
    f.write("Hello, file!")
```

**JavaScript (Node.js)**
```javascript
// console output
console.log("Hello, file!");

// file I/O (Node.js)
import fs from "fs/promises";

const contents = await fs.readFile("data.txt", "utf-8");
await fs.writeFile("output.txt", "Hello, file!");
```

**Apply it when:** any time your program needs to interact with the
outside world — this is how programs stop being closed loops and start
doing useful work with real data.

> **Related code in this repo:** [`Python/Data_Fundamentals/File_Handling/`](Python/Data_Fundamentals/File_Handling/) covers the file-I/O half of this section in depth — one dedicated file per mode (`r.py`, `w.py`, `a.py`, `x.py`, `b.py`), each demonstrating a genuinely different failure case.

---

## 12. Exceptions (try/catch)

When something goes wrong, a program can **throw/raise** an exception,
which interrupts normal flow until something **catches** it — otherwise
the program crashes. This becomes essential the moment you're doing real
I/O (Section 11) — files might not exist, input might be malformed,
networks fail.

**Python**
```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Can't divide by zero")
        return None
    finally:
        print("This always runs")

divide(10, 0)
```

**JavaScript**
```javascript
function divide(a, b) {
  try {
    if (b === 0) throw new Error("Can't divide by zero");
    return a / b;
  } catch (error) {
    console.log(error.message);
    return null;
  } finally {
    console.log("This always runs");
  }
}

divide(10, 0);
```

**Apply it when:** something might fail in a way you can't fully prevent
(network calls, file access, user input, division by zero) — wrap it so
one failure doesn't crash the whole program.

---

## 13. Modules & Packages

As programs grow, code gets split across files (modules) and reusable
groups of files (packages/libraries) that can be imported where needed.

**Python**
```python
# math_utils.py
def add(a, b):
    return a + b

# main.py
from math_utils import add
print(add(2, 3))  # 5

# using an installed package
import requests
response = requests.get("https://example.com")
```

**JavaScript**
```javascript
// mathUtils.js
export function add(a, b) {
  return a + b;
}

// main.js
import { add } from "./mathUtils.js";
console.log(add(2, 3)); // 5

// using an installed package (Node.js)
import axios from "axios";
const response = await axios.get("https://example.com");
```

**Apply it when:** a single file grows past a few hundred lines, or a
piece of logic (auth, date formatting, API calls) is used in more than
one place — pull it into its own module.

---

## 14. APIs & Libraries

An API (Application Programming Interface) is a defined way for one
piece of code to talk to another — your code calling a library function,
or your code calling a remote web service over HTTP. This is where the
Modules skill above (13) meets the outside world.

**Python**
```python
import requests

response = requests.get("https://api.example.com/users")
if response.status_code == 200:
    users = response.json()
    print(users)
```

**JavaScript**
```javascript
const response = await fetch("https://api.example.com/users");
if (response.ok) {
  const users = await response.json();
  console.log(users);
}
```

**Apply it when:** you need functionality someone else has already
built (don't write your own date-parsing library) or your app needs data
that lives on another server (weather data, payment processing, your own
backend).

---

# Phase 4 — Deeper Concepts

*Goal: understand *why* your code behaves the way it does. These
concepts are much easier to absorb now that you've hit real bugs they
explain — a mysteriously mutated list, a weird type coercion, a program
that "still remembers" something it shouldn't.*

## 15. Recursion

A function that calls itself, typically to break a problem into smaller
versions of the same problem. Every recursive function needs a **base
case** (when to stop) or it will run forever (and crash with a stack
overflow).

**Python**
```python
def factorial(n):
    if n <= 1:          # base case
        return 1
    return n * factorial(n - 1)  # recursive case

print(factorial(5))  # 120
```

**JavaScript**
```javascript
function factorial(n) {
  if (n <= 1) return 1;          // base case
  return n * factorial(n - 1);   // recursive case
}

console.log(factorial(5)); // 120
```

**Apply it when:** the problem is naturally self-similar — tree/graph
traversal, parsing nested structures (JSON, file systems), divide-and-
conquer algorithms. For simple counting/repetition, a loop is usually
clearer and more efficient.

> **Related code in this repo:** [`Python/Data_Fundamentals/Algorithms/BFS/bfs.py`](Python/Data_Fundamentals/Algorithms/BFS/bfs.py) and [`DFS/dfs.py`](Python/Data_Fundamentals/Algorithms/DFS/dfs.py) put this to work — DFS in particular is commonly written recursively, using the call stack instead of an explicit one.
>
> Once plain recursion clicks, the natural next step is **Dynamic
> Programming** — recursion plus a memory for subproblems you've already
> solved. See [`Python/Data_Fundamentals/Algorithms/Dynamic_Programming/dynamic_programming.md`](Python/Data_Fundamentals/Algorithms/Dynamic_Programming/dynamic_programming.md)
> for memoization vs. tabulation, worked through end-to-end with the
> Fibonacci example (brute force → memoized → tabulated → space-optimized).

---

## 16. Type Systems

**Static vs. dynamic:** in a *statically* typed language, a variable's
type is fixed and checked before the program runs (Java, C++, TypeScript).
In a *dynamically* typed language, types are checked at runtime, and a
variable can hold different types over its life (Python, JavaScript).

**Strong vs. weak:** a *strongly* typed language won't silently convert
incompatible types for you. A *weakly* typed one will.

Python and JavaScript are both dynamically typed, but Python is strong and
JavaScript is famously weak:

```python
# Python — dynamic but strong: this raises an error
"5" + 5   # TypeError: can only concatenate str (not "int") to str
```

```javascript
// JavaScript — dynamic and weak: this silently coerces
"5" + 5   // "55" (number converted to string)
"5" - 5   // 0 (string converted to number — inconsistent with above!)
```

**Apply it when:** debugging type-related bugs — in JS, always ask
"is this being silently coerced?" before assuming a bug is elsewhere.
In Python, if you get a `TypeError`, the language is protecting you by
refusing to guess.

> **Related code in this repo:** [`Python/Data_Fundamentals/Type_Systems/typesSystem.py`](Python/Data_Fundamentals/Type_Systems/typesSystem.py) works through the Python side of this section on its own, without the JavaScript comparison.

---

## 17. Pointers & References

A pointer/reference is a value that *points to* where data lives in
memory, rather than being the data itself. Python and JavaScript hide
raw pointers from you, but the underlying concept still matters.

It's tempting to summarize the rule as "objects are passed by reference,
primitives are passed by value" — and the examples below will look like
they confirm exactly that. But that phrasing overpromises: in a language
with *true* pass-by-reference (like a C++ reference parameter), reassigning
the parameter inside the function *also* rebinds the caller's variable.
That's not what happens in Python or JavaScript. Both actually use what's
more precisely called **pass by object reference** (or "call by
sharing"): the function gets a copy of the *reference itself*, not the
object. That copy is enough to reach into the object and mutate it — but
reassigning the parameter to point at something new only changes the
local copy, leaving the caller's variable untouched. The two examples
below show both halves of that rule side by side, which is what makes it
click:

**Python**
```python
def modify_list(lst):
    lst.append(4)  # mutates the shared object — visible to the caller

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [1, 2, 3, 4] — changed!

def reassign_list(lst):
    lst = [9, 9, 9]  # rebinds the LOCAL name only — caller's list is untouched

reassign_list(my_list)
print(my_list)  # [1, 2, 3, 4] — unchanged!

def modify_number(n):
    n += 1  # numbers are immutable — this can only ever rebind locally

x = 5
modify_number(x)
print(x)  # 5 — unchanged
```

**JavaScript**
```javascript
function modifyArray(arr) {
  arr.push(4); // mutates the shared object — visible to the caller
}

const myArray = [1, 2, 3];
modifyArray(myArray);
console.log(myArray); // [1, 2, 3, 4] — changed!

function reassignArray(arr) {
  arr = [9, 9, 9]; // rebinds the LOCAL name only — caller's array is untouched
}

reassignArray(myArray);
console.log(myArray); // [1, 2, 3, 4] — unchanged!

function modifyNumber(n) {
  n += 1; // primitives are immutable — this can only ever rebind locally
}

let x = 5;
modifyNumber(x);
console.log(x); // 5 — unchanged
```

**Apply it when:** debugging "why did my object change when I didn't
mean it to?" bugs — this is almost always because you passed a
reference (object/array/dict) and *mutated* it somewhere, rather than
reassigned it. If you instead wanted a change to be invisible to the
caller, mutating in place was the mistake — build and return a new
object instead.

---

## 18. Memory Management

Every value your program creates needs memory. The **stack** holds small,
fixed-size data with a predictable lifetime (like local variables in a
function call). The **heap** holds larger or longer-lived data (objects,
arrays) that needs to stick around after a function returns.

Python and JavaScript both use **automatic memory management**
(garbage collection) — you don't manually free memory; the runtime
detects when something is no longer reachable and reclaims it. This is
very different from C/C++, where you allocate and free memory yourself.

```python
def make_list():
    local_list = [1, 2, 3]  # allocated on the heap
    return local_list       # reference survives — GC won't collect it

data = make_list()  # still reachable, still alive
# once `data` goes out of scope and nothing else references it,
# Python's garbage collector reclaims the memory automatically
```

```javascript
function makeArray() {
  const localArray = [1, 2, 3]; // allocated on the heap
  return localArray;             // reference survives
}

let data = makeArray(); // still reachable
data = null; // no more references — eligible for garbage collection
```

**Apply it when:** you don't manually manage this in Python/JS, but
understanding it explains memory leaks — e.g., holding onto references
you don't need (event listeners never removed, large objects stored in a
global cache) prevents the garbage collector from freeing them.

---

# Phase 5 — Paradigms & Advanced Patterns

*Goal: see the ways of organizing everything you already know. These
click much harder once you've felt the pain they solve — messy globals
that OOP's encapsulation fixes, hard-to-test side-effecty code that
functional purity fixes.*

## 19. Object-Oriented Programming

Bundles data and the functions that operate on it into **objects**,
created from **classes**. Core ideas: encapsulation (bundling
data + behavior), inheritance (a class reusing/extending another), and
polymorphism (different classes responding to the same method call in
their own way).

**Python**
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):          # inheritance
    def speak(self):        # polymorphism — overrides parent
        return f"{self.name} barks"

animals = [Animal("Generic"), Dog("Rex")]
for a in animals:
    print(a.speak())
# Generic makes a sound
# Rex barks
```

**JavaScript**
```javascript
class Animal {
  constructor(name) {
    this.name = name;
  }
  speak() {
    return `${this.name} makes a sound`;
  }
}

class Dog extends Animal {       // inheritance
  speak() {                       // polymorphism
    return `${this.name} barks`;
  }
}

const animals = [new Animal("Generic"), new Dog("Rex")];
animals.forEach(a => console.log(a.speak()));
// Generic makes a sound
// Rex barks
```

**Apply it when:** modeling real-world entities with clear identity and
behavior (users, orders, game characters) — especially when you have
many related "kinds" of something that share behavior but differ in
specifics.

---

## 20. Functional Programming

Treats computation as the evaluation of **pure functions** — functions
that always return the same output for the same input and don't modify
anything outside themselves (no side effects). Favors **immutability**
(not changing data in place) and composing small functions together.

**Python**
```python
numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda n: n * 2, numbers))
evens = list(filter(lambda n: n % 2 == 0, numbers))
total = sum(numbers)  # a "reduce" in effect

# pure function — no side effects, same input always gives same output
def add(a, b):
    return a + b
```

**JavaScript**
```javascript
const numbers = [1, 2, 3, 4, 5];

const doubled = numbers.map(n => n * 2);
const evens = numbers.filter(n => n % 2 === 0);
const total = numbers.reduce((sum, n) => sum + n, 0);

// pure function
const add = (a, b) => a + b;
```

**Apply it when:** transforming collections of data (map/filter/reduce
chains are often clearer than manual loops), or whenever you want code
that's easy to test and reason about because it has no hidden state.

---

## 21. Error-as-Value

Some languages (Go, Rust) avoid exceptions entirely and instead return an
error *as a normal value* the caller must explicitly check. Python and
JavaScript are exception-based by default (Section 12), but this pattern
still shows up — e.g., a function returning `None`/`null` to signal
failure, or an API response object with a `success`/`error` field. It's
placed last because it's really a *design choice* layered on top of
everything above it, not a new primitive concept.

```python
def safe_divide(a, b):
    if b == 0:
        return None, "Cannot divide by zero"
    return a / b, None

result, error = safe_divide(10, 0)
if error:
    print(error)
else:
    print(result)
```

```javascript
function safeDivide(a, b) {
  if (b === 0) return { result: null, error: "Cannot divide by zero" };
  return { result: a / b, error: null };
}

const { result, error } = safeDivide(10, 0);
if (error) {
  console.log(error);
} else {
  console.log(result);
}
```

**Apply it when:** you want failure handling to be explicit and forced —
this pattern is common in APIs and async operations where "silently
ignoring an error" is dangerous.

---

## How to Use This Reference

1. **Work through the phases in order the first time.** Phase 1 alone is
   enough to write real, if clumsy, programs — don't skip ahead to
   Phase 5 looking for "the good stuff." OOP and FP are much easier to
   appreciate once you've felt the problems they solve.
2. **Don't memorize syntax — understand the concept first.** Once you
   know *what* a closure or a pure function *is*, the syntax for it in
   any new language is a five-minute lookup.
3. **When learning a new language, map it against this list.** Ask: how
   does this language do loops? Conditionals? Error handling? Is it
   statically or dynamically typed? You'll find you already know most of
   the "shape" of the language before writing a line of it.
4. **Use this as a debugging checklist**, out of order, once you've
   finished it once. Stuck on unexpected behavior? Check: is this a
   scope issue (8)? A reference vs. value issue (17)? A type coercion
   issue (16, especially in JS)? Most bugs trace back to one of the
   sections above.
5. **Practice by porting code.** Take a small script you've written in
   Python and rewrite it in JavaScript (or vice versa) using this guide
   section by section — it's one of the fastest ways to cement both
   languages at once.
6. **Follow a "Related code in this repo" link when you see one**, and
   actually run the file rather than just reading it — this guide tells
   you what a concept *is*, but the linked scripts under `Python/` are
   where you confirm it for yourself with real, printed output.

## Contributing

Sections without a **Related code in this repo** callout (Functions,
Scope & Lifetime, Input/Output's console half, Exceptions, Modules &
Packages, APIs & Libraries, Type Systems' JS comparison, Memory
Management, OOP, Functional Programming, Error-as-Value) don't have a
dedicated, runnable folder yet. If you'd like to add one:

- Follow the pattern already established under `Python/Data_Fundamentals/`
  and `Python/Control_Flows/`: one concept per file, runnable
  standalone, with `print()` output and comments explaining *why*, not
  just *what*.
- Add a matching entry to that folder's own `README.md`, in its
  suggested learning order.
- Come back to this file and add a **Related code in this repo** callout
  under the matching section, pointing at the new file.

Pull requests, issue reports, and beginner questions are all welcome.