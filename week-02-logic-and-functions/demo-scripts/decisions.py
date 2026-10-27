"""Session 2.1 demo — if / elif / else and comparison + logical operators."""

temperature = 28

if temperature >= 30:
    print("Hot - stay hydrated")
elif temperature >= 20:
    print("Pleasant")
elif temperature >= 10:
    print("Cool - bring a jacket")
else:
    print("Cold")

# Logical operators combine conditions.
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("Entry allowed")

if not has_ticket:
    print("Please buy a ticket")

# Comparison returns a boolean
print(5 == 5, 5 != 4, 3 < 2)
