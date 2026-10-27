"""Session 3.1 demo — OS-agnostic paths with pathlib."""

from pathlib import Path

# Build paths with / — works on every OS.
folder = Path("reports")
file_path = folder / "june" / "summary.txt"
print("Path:", file_path)

# Inspect parts of a path
p = Path("archive/data_2026.csv")
print("name:", p.name)       # data_2026.csv
print("stem:", p.stem)       # data_2026
print("suffix:", p.suffix)   # .csv
print("parent:", p.parent)   # archive

# Current directory and existence checks
here = Path(".")
print("Exists?", here.exists())

# List files in the current directory (first 5)
print("--- items here ---")
for item in list(here.iterdir())[:5]:
    kind = "DIR " if item.is_dir() else "FILE"
    print(kind, item.name)
