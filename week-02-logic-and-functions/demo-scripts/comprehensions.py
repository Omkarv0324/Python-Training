"""Session 2.3 demo — list and dict comprehensions."""

numbers = [1, 2, 3, 4, 5, 6]

# Transform: double each
doubled = [n * 2 for n in numbers]
print(doubled)

# Filter: keep evens only
evens = [n for n in numbers if n % 2 == 0]
print(evens)

# Transform + filter together
squares_of_odds = [n * n for n in numbers if n % 2 == 1]
print(squares_of_odds)

# Dict comprehension
name_lengths = {name: len(name) for name in ["Ada", "Alan", "Grace"]}
print(name_lengths)
