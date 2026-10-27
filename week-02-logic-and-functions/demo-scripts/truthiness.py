"""Session 2.1 demo — truthiness: what counts as True/False in a condition."""

# These are all "falsy":
for value in [0, 0.0, "", [], {}, set(), None, False]:
    if value:
        print(repr(value), "-> truthy")
    else:
        print(repr(value), "-> falsy")

# Common real-world use: check if a list has anything in it.
items = []
if items:
    print("Processing items...")
else:
    print("Nothing to process")
