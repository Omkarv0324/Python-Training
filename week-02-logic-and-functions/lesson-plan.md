# Week 2 — Logic, Loops & Reusable Code · Lesson Plans (Breadth-First)

Five topic-dense, demo-driven sessions. Instructor explains + runs demos; learners keep
the takeaways. Exercises are optional homework. OS-agnostic.

---

## Session 2.1 — Decisions: `if` / `elif` / `else`, Comparison & Logical Operators

**Topics covered**
- Booleans recap; comparison operators `== != < > <= >=`
- `if` / `elif` / `else` structure and indentation
- Logical operators `and`, `or`, `not`
- Truthiness: what counts as "falsy" (`0`, `""`, `[]`, `None`)
- Nesting vs flat conditions (readability)

**Demos to run:** `demo-scripts/decisions.py`, `demo-scripts/truthiness.py`

**Real-world framing:** Automation makes decisions constantly — "if the file exists, skip
it," "if the value is over threshold, alert." Conditions are the branching logic of every
useful script.

**Takeaways**
- Indentation defines blocks in Python — be consistent (4 spaces).
- `==` compares values; `=` assigns. Don't mix them up.
- Empty/zero/`None` values are "falsy"; most else is "truthy".

---

## Session 2.2 — `for` Loops & `range()`

**Topics covered**
- `for item in sequence:` over lists, strings, dicts
- `range(stop)`, `range(start, stop)`, `range(start, stop, step)`
- `enumerate()` for index + value
- Accumulator pattern (building a sum/total/list)
- Looping over `dict.items()`

**Demos to run:** `demo-scripts/for_loops.py`, `demo-scripts/accumulate.py`

**Real-world framing:** Batch processing is automation's bread and butter — loop over every
file, row, or record and do the same thing to each.

**Takeaways**
- `for x in things:` runs the body once per item.
- `range(n)` gives 0..n-1; add a step for counting by 2s, backwards, etc.
- `enumerate(things)` gives `(index, value)` pairs.

---

## Session 2.3 — `while` Loops, `break`/`continue`, Comprehensions

**Topics covered**
- `while condition:` and avoiding infinite loops
- `break` (stop early) and `continue` (skip to next iteration)
- The "loop until valid input" pattern
- List comprehensions: `[x*2 for x in items]`
- Filtered comprehensions: `[x for x in items if ...]`; dict comprehensions

**Demos to run:** `demo-scripts/while_loops.py`, `demo-scripts/comprehensions.py`

**Real-world framing:** `while` loops retry until something succeeds (polling an API, waiting
for a file). Comprehensions transform/filter a whole collection in one readable line.

**Takeaways**
- `while` repeats until its condition is false — always change something inside.
- `break` exits the loop; `continue` skips to the next iteration.
- `[expr for x in seq if cond]` is a compact transform+filter.

---

## Session 2.4 — Functions: Define, Params, Returns, Defaults, Scope

**Topics covered**
- `def name(params):` and calling functions
- Arguments vs parameters; positional vs keyword
- `return` values (and functions that return `None`)
- Default parameter values
- Local vs global scope; why globals are risky
- Docstrings for functions

**Demos to run:** `demo-scripts/functions_basics.py`, `demo-scripts/scope.py`

**Real-world framing:** Functions turn a working snippet into a reusable tool. Automation
grows by composing small, named, testable functions instead of copy-pasting.

**Takeaways**
- Define once, call many times: DRY (Don't Repeat Yourself).
- `return` hands a value back; without it you get `None`.
- Variables inside a function are local — they don't leak out.

---

## Session 2.5 — `*args`/`**kwargs`, Lambdas & a Reusable Helper Module

**Topics covered**
- Flexible arguments: `*args` (extra positionals), `**kwargs` (extra keywords)
- `lambda` one-line functions; using them with `sorted(key=...)`
- Putting functions in a `.py` file and importing them (`import helpers`)
- `if __name__ == "__main__":` guard
- A quick look ahead: this helper module seeds the Week 3 capstone

**Demos to run:** `demo-scripts/args_kwargs.py`, `demo-scripts/lambdas.py`,
`demo-scripts/helpers.py`, `demo-scripts/use_helpers.py`

**Real-world framing:** Real automation lives in reusable modules you import across scripts.
A small, well-named helper library pays off every week.

**Takeaways**
- `*args`/`**kwargs` accept any number of extra arguments.
- `lambda x: x*2` is a tiny inline function — handy for `sorted`/`map`/`filter`.
- Put reusable functions in a module and `import` it; guard runnable code with
  `if __name__ == "__main__":`.

---

### Week 2 recap slide (use at start of Week 3)
You can now branch with `if`, repeat with `for`/`while`, transform with comprehensions, and
package logic into reusable functions and modules. Next: making scripts touch the real
world — files, data formats, errors, and external tools.
