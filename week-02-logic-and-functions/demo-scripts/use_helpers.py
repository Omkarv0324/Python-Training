"""Session 2.5 demo — importing and using our helper module.

Run from the demo-scripts folder so `import helpers` finds helpers.py:
    python use_helpers.py
"""

import helpers

names = ["  ada LOVELACE ", "alan TURING", " grace hopper "]

for raw in names:
    clean = helpers.clean_name(raw)
    file_slug = helpers.slugify(clean) + ".txt"
    print(f"{clean}  ->  {file_slug}")

print("Pass rate:", helpers.percent(7, 10), "%")
