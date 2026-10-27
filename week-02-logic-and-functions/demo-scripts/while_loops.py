"""Session 2.3 demo — while loops, break, continue."""

# Count down
n = 3
while n > 0:
    print("T-minus", n)
    n = n - 1          # MUST change, or infinite loop!
print("Liftoff!")

# break: stop early
for i in range(100):
    if i == 5:
        break
    print("i =", i)

# continue: skip this iteration
for i in range(6):
    if i % 2 == 0:
        continue       # skip evens
    print("odd:", i)
