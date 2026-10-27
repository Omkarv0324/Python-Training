# Week 2 — Homework Solutions

## Session 2.1
```python
# Core
n = int(input("Number: "))
if n > 0:
    print("positive")
elif n < 0:
    print("negative")
else:
    print("zero")

# Stretch
score = int(input("Score: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# Bonus
age, has_ticket = 20, True
if age >= 18 and has_ticket:
    print("entry allowed")
```

## Session 2.2
```python
# Core
for i in range(1, 11):
    print(i)

# Stretch
total = 0
for i in range(1, 101):
    total += i
print(total)   # 5050

# Bonus
tasks = ["email", "standup", "code", "review"]
for i, t in enumerate(tasks, start=1):
    print(i, t)
```

## Session 2.3
```python
# Core
n = 5
while n > 0:
    print(n)
    n -= 1
print("Go!")

# Stretch
print([n * n for n in range(1, 11)])

# Bonus
nums = [1, 2, 3, 4, 5, 6]
print([n for n in nums if n % 2 == 0])
```

## Session 2.4
```python
# Core
def area(width, height):
    return width * height
print(area(3, 4))
print(area(10, 2))

# Stretch
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
print(greet("Ada"))
print(greet("Ada", "Hi"))

# Bonus
def is_even(n):
    return n % 2 == 0
for n in range(1, 11):
    print(n, is_even(n))
```

## Session 2.5
```python
# Core
def total(*args):
    return sum(args)
print(total(1, 2, 3, 4))

# Stretch
people = [("Ada", 36), ("Alan", 41), ("Grace", 29)]
print(sorted(people, key=lambda p: p[1]))

# Bonus
# myutils.py
def shout(s): return s.upper()
def whisper(s): return s.lower()
# other script:
# import myutils
# print(myutils.shout("hi"))
```
