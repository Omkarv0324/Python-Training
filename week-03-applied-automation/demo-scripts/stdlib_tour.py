"""Session 3.4 demo — a quick tour of handy standard-library modules."""

import datetime
import random
from collections import Counter

# datetime: today's date and formatting
today = datetime.date.today()
print("Today:", today)
print("Formatted:", today.strftime("%A, %B %d, %Y"))

now = datetime.datetime.now()
print("Timestamp:", now.strftime("%Y-%m-%d %H:%M:%S"))

# random: picking and shuffling
random.seed(42)  # makes output reproducible for the demo
print("Dice roll:", random.randint(1, 6))
print("Pick:", random.choice(["red", "green", "blue"]))

# collections.Counter: tally things fast
words = "the cat sat on the mat the end".split()
counts = Counter(words)
print("Word counts:", counts)
print("Most common:", counts.most_common(1))
