"""Session 4.2 demo — dunder (magic) methods make objects behave like built-ins."""


class Money:
    def __init__(self, cents):
        self.cents = cents

    # Readable debug output
    def __repr__(self):
        return f"Money({self.cents})"

    # Friendly string for print()
    def __str__(self):
        return f"${self.cents / 100:.2f}"

    # Equality
    def __eq__(self, other):
        return isinstance(other, Money) and self.cents == other.cents

    # Ordering (enables sorting, <, >, etc. with @total_ordering or all methods)
    def __lt__(self, other):
        return self.cents < other.cents

    # Addition
    def __add__(self, other):
        return Money(self.cents + other.cents)


a = Money(1050)   # $10.50
b = Money(250)    # $2.50

print(str(a))             # $10.50   (uses __str__)
print(repr(b))            # Money(250)
print(a == Money(1050))   # True     (uses __eq__)
print(a + b)              # $13.00   (uses __add__ then __str__)
print(sorted([a, b]))     # sorted via __lt__ -> [$2.50 .. ] shown as repr list
