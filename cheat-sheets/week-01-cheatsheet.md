# Week 1 Cheat Sheet — Foundations & Core Data

## Running Python
```
python --version        # Windows
python3 --version       # macOS/Linux
python hello.py         # run a script
python                  # start the REPL (exit() to quit)
```

## Output & comments
```python
print("Hello", 42)      # Hello 42
# this is a comment
```

## Variables & types
```python
name = "Ada"            # str
count = 5               # int
price = 9.99            # float
active = True           # bool
type(price)             # <class 'float'>
```

## Numbers
```python
+  -  *  /              # /  -> float
//   %   **             # floor div, remainder, power
round(3.14159, 2)       # 3.14
int("5"), float("2.5"), str(10)   # conversions
```

## Strings
```python
s = "hello world"
len(s)                  # 11
s[0], s[-1]             # 'h', 'd'
s[0:5]                  # 'hello'  (slicing)
s[::-1]                 # reverse
s.upper() s.lower() s.title() s.strip()
s.replace("world", "there")
s.split(" ")            # ['hello', 'world']
f"{name} is {count}"    # f-string
f"{price:.2f}"          # 2 decimals
```

## Input
```python
x = input("Name: ")         # always a string
n = int(input("Age: "))     # convert for math
```

## Lists & tuples
```python
items = [1, 2, 3]
items.append(4); items.pop(); items[0]; items[-1]
items[1:3]; len(items); 2 in items

point = (3, 4)          # tuple (immutable)
x, y = point            # unpack
```

## Dicts & sets
```python
user = {"name": "Ada", "age": 36}
user["name"]; user.get("city", "n/a")
user["city"] = "London"
for k, v in user.items(): ...

unique = set([1, 1, 2])     # {1, 2}
"a" in unique
a | b, a & b, a - b         # union, intersection, difference
```
