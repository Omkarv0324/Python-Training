"""Session 1.4 demo — tuples and unpacking."""

# A tuple is an ordered, FIXED (immutable) group of values.
point = (3, 4)
print("x:", point[0], "y:", point[1])

# Unpacking: assign each element to a variable at once.
x, y = point
print("Unpacked:", x, y)

# Great for fixed records that shouldn't change.
rgb = (255, 128, 0)
r, g, b = rgb
print(f"R={r} G={g} B={b}")

# Trying to change a tuple raises an error (uncomment to show):
# point[0] = 9  # TypeError: 'tuple' object does not support item assignment
