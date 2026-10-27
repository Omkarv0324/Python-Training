# Overflow Bank — Extra Challenges + Deferred Advanced Topics

Your "never run out of material" safety net. Two sections:

1. **Mini-challenge parking lot** — standalone problems, sorted by topic. Throw one out any
   time a session runs short or a fast group needs more.
2. **Deferred advanced topics** — ready-to-teach bonus modules (OOP depth, testing, web
   scraping, Git) if you have spare sessions or want enrichment/homework.

---

# Part 1 — Mini-Challenge Parking Lot

Each is small (2–10 minutes). No setup needed beyond Python.

## Printing & output
- Print a 5-row triangle of `*` (1 star, then 2, …).
- Print a multiplication table for 7 (7×1 … 7×10).
- Print today's date three different ways.

## Numbers & math
- Convert Celsius to Fahrenheit for 0, 25, 37, 100.
- Given a total of seconds, print `H:MM:SS`.
- Check if a number is even using `%`.
- Compute compound interest for a principal over N years.

## Strings & text
- Count the vowels in a sentence.
- Reverse each word in a sentence but keep word order.
- Check if a word is a palindrome.
- Turn "first last" into "Last, First".
- Mask all but the last 4 digits of a card number.

## Lists & loops
- Find the largest number in a list without `max()`.
- Remove duplicates from a list while preserving order.
- Given a list of prices, print the total and the average.
- Flatten a list of lists into one list.
- Count how many words in a list start with a vowel.

## Dicts & sets
- Count word frequency in a paragraph (dict).
- Merge two dicts; on key conflict, keep the larger value.
- Given two lists of IDs, print the ones in both (set intersection).
- Invert a dict (swap keys and values).

## Conditions & logic
- FizzBuzz 1–30.
- Classify a year as leap year or not.
- Given a time (0–23), print "morning/afternoon/evening/night".

## Functions
- Write `is_prime(n)`.
- Write `celsius_to_f(c)` and `f_to_celsius(f)` and verify they round-trip.
- Write a function that returns the min and max of a list as a tuple.
- Write `clamp(value, low, high)`.

## Files & automation
- Count the lines, words, and characters in a text file.
- Read a file and write a copy with line numbers prepended.
- Find all `.txt` files in a folder with `pathlib` and print their sizes.
- Read a CSV of sales and print the total per category.
- Write a script that creates dated backup filenames.

## Errors
- Wrap `int(input())` so bad input re-prompts until valid.
- Read a file that might not exist and print a friendly message instead of crashing.

---

# Part 2 — Deferred Advanced Topics (bonus modules)

These were intentionally kept out of the 15 core sessions to protect pacing for beginners.
Each is a self-contained ~1-hour enrichment block you can run if time allows or assign as
guided homework.

## A. OOP, deeper
- Instance vs class attributes.
- `@property` getters, `@staticmethod`, `@classmethod`.
- Inheritance and method overriding; `super()`.
- Dunder methods: `__repr__`, `__eq__`, `__len__`.
- `@dataclass` for boilerplate-free data classes.

**Demo seed**
```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
    def distance_to_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

print(Point(3, 4).distance_to_origin())   # 5.0
```

## B. Testing with pytest
- Why tests: confidence to change automation safely.
- `pip install pytest`; name files `test_*.py`.
- `assert` statements; running `pytest -q`.
- Testing functions from the Week 2 helper module.

**Demo seed** (`test_helpers.py`)
```python
from helpers import slugify, percent

def test_slugify():
    assert slugify("My Report 2026") == "my_report_2026"

def test_percent():
    assert percent(3, 8) == 37.5
    assert percent(1, 0) == 0.0
```
Run: `pytest -q`

## C. Web scraping
- `requests` to fetch a page; `BeautifulSoup` (`pip install beautifulsoup4`) to parse HTML.
- Selecting elements: `soup.find`, `soup.find_all`, CSS selectors.
- Etiquette: respect `robots.txt`, rate-limit, prefer official APIs.

**Demo seed**
```python
import requests
from bs4 import BeautifulSoup

html = requests.get("https://example.com", timeout=5).text
soup = BeautifulSoup(html, "html.parser")
print(soup.title.string)
for link in soup.find_all("a"):
    print(link.get("href"))
```

## D. Git basics (saving & sharing work)
- Why version control: history, backup, collaboration.
- Core loop: `git init`, `git add`, `git commit -m "..."`, `git status`, `git log`.
- Connecting to a remote: `git remote add origin <url>`, `git push`.
- A sensible `.gitignore` for Python (`.venv/`, `__pycache__/`, `*.pyc`).

**Cheat seed**
```
git init
git add .
git commit -m "Initial commit"
git remote add origin <url>
git push -u origin main
```

## E. Other directions to mention (1-line each)
- Scheduling: `cron` (macOS/Linux) / Task Scheduler (Windows) to run scripts automatically.
- Spreadsheets: `openpyxl` to read/write real `.xlsx` files.
- Type hints: `def f(x: int) -> str:` for clarity and tooling.
- Virtualenv managers: `uv` / `poetry` for modern dependency management.
- `argparse` for proper command-line interfaces.

---

## "Break My Code" bank (infinite debugging drill)
Paste one, ask the class to find the bug:

```python
# 1. Off-by-one / wrong comparison
for i in range(1, 5):
    print(i)          # expected 1..5 — why only 1..4?

# 2. input returns a string
age = input("age: ")
print(age + 1)        # TypeError — fix it

# 3. Mutable default / reassign confusion
def add(item, bag=[]):
    bag.append(item)
    return bag        # why does the list grow across calls?

# 4. Indentation / scope
def total(nums):
    s = 0
    for n in nums:
        s += n
    return s          # move return out one level — what changes?

# 5. Dict KeyError
config = {"host": "localhost"}
print(config["port"])   # KeyError — use .get()
```
