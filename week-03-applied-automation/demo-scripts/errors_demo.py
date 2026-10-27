"""Session 3.3 demo — try/except/else/finally, specific exceptions, raise."""


def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Can't divide by zero — returning None")
        return None
    else:
        # runs only if no exception
        print("Division succeeded")
        return result
    finally:
        # always runs
        print("(cleanup done)")


print(safe_divide(10, 2))
print(safe_divide(10, 0))


# Catch specific exceptions
def read_number(text):
    try:
        return int(text)
    except ValueError:
        print(f"'{text}' is not a valid integer")
        return 0


print(read_number("42"))
print(read_number("oops"))


# Raise your own error for invalid input
def set_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age


try:
    set_age(-5)
except ValueError as e:
    print("Caught:", e)
