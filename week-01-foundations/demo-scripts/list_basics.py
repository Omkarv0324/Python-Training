"""Session 1.5 demo — lists and a gentle first for-loop."""

# A list holds many items in order.
fruits = ["apple", "banana", "cherry"]

# Indexing: first is [0], last is [-1]
print("First:", fruits[0])
print("Last:", fruits[-1])
print("How many:", len(fruits))

# Add to the end
fruits.append("date")
print("After append:", fruits)

# Loop over every item
for fruit in fruits:
    print("I like", fruit)
