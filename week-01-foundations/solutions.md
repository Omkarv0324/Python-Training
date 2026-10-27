# Week 1 — Homework Solutions

## Session 1.1
```python
# Core
print("Ada Lovelace")
print("London")
print("Learning Python!")

# Stretch
name = "Ada Lovelace"
city = "London"
msg = "Learning Python!"
print(name)
print(city)
print(msg)

# Bonus
print("=" * 40)
print("        MY STARTUP CHECKLIST")
print("=" * 40)
print("[ ] Coffee")
print("[ ] Check calendar")
print("[ ] Review PRs")
print("[ ] Deep work")
```

## Session 1.2
```python
# Core
width = 7
height = 3
print("Area:", width * height)

# Stretch
bill = 84.50
tip = bill * 0.15
print("Tip:", round(tip, 2))
print("Total:", round(bill + tip, 2))

# Bonus
seconds = 5000
print(seconds // 60, "minutes", seconds % 60, "seconds")
```

## Session 1.3
```python
# Core
first = input("First name: ")
last = input("Last name: ")
full = first + " " + last
print("Full name:", full)
print("Length:", len(full))

# Stretch
year = int(input("Birth year: "))
print("Age in 2026:", 2026 - year)

# Bonus
name = input("Full name: ")
print("Reversed:", name[::-1])
```

## Session 1.4
```python
# Core
tasks = ["email", "standup", "code", "review"]
tasks.append("deploy")
print(tasks)
print("Count:", len(tasks))

# Stretch
print("First:", tasks[0])
print("Last:", tasks[-1])

# Bonus
point = (3, 4)
x, y = point
print("x:", x, "y:", y)
```

## Session 1.5
```python
# Core
book = {"title": "Dune", "author": "Herbert", "year": 1965}
for key, value in book.items():
    print(f"{key}: {value}")

# Stretch
print(book.get("pages", "unknown"))

# Bonus
nums = [1, 1, 2, 3, 3, 3, 4]
print(set(nums))
```
