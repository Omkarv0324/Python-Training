"""Session 1.5 demo — sets (unique items + fast membership + set math)."""

# A set stores only UNIQUE items.
ids = [1, 2, 2, 3, 3, 3]
unique_ids = set(ids)
print("Unique:", unique_ids)   # {1, 2, 3}

# Fast membership test
seen = {"a@x.com", "b@x.com"}
print("a@x.com" in seen)        # True

# Set math
monday = {"alice", "bob", "carol"}
tuesday = {"bob", "dave"}
print("Both days:", monday & tuesday)   # intersection
print("Either day:", monday | tuesday)  # union
print("Monday only:", monday - tuesday) # difference
