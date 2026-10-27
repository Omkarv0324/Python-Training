"""Session 2.4 demo — defining functions, params, returns, defaults."""


def greet(name):
    """Return a greeting string."""
    return f"Hello, {name}!"


def add(a, b):
    return a + b


def power(base, exponent=2):
    """exponent defaults to 2 if not given."""
    return base ** exponent


print(greet("Ada"))
print("Sum:", add(3, 4))
print("Square:", power(5))       # uses default exponent=2
print("Cube:", power(5, 3))      # override default

# A function with no return gives back None
def shout(text):
    print(text.upper())

result = shout("hi")
print("Return value:", result)   # None
