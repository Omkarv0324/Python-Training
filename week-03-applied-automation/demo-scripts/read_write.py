"""Session 3.1 demo — reading, writing, and appending text files."""

# Write (overwrites any existing file)
with open("notes.txt", "w") as f:
    f.write("First line\n")
    f.write("Second line\n")

# Append (adds to the end)
with open("notes.txt", "a") as f:
    f.write("Third line (appended)\n")

# Read the whole file
with open("notes.txt", "r") as f:
    content = f.read()
print("--- full content ---")
print(content)

# Read line by line (memory-friendly for big files)
print("--- line by line ---")
with open("notes.txt", "r") as f:
    for line in f:
        print(line.rstrip())

# Clean up the demo file
import os
os.remove("notes.txt")
