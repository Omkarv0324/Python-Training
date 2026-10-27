"""Session 2.2 demo — the accumulator pattern (build up a result in a loop)."""

numbers = [10, 20, 30, 40]

# Sum
total = 0
for n in numbers:
    total = total + n
print("Total:", total)

# Build a new list
doubled = []
for n in numbers:
    doubled.append(n * 2)
print("Doubled:", doubled)

# Count things that match
big = 0
for n in numbers:
    if n >= 30:
        big = big + 1
print("Count >= 30:", big)
