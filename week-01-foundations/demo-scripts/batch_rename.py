"""Session 1.5 automation mini-task — clean + number a batch of filenames.

Combines Week 1 skills: lists, strings, f-strings, and a for-loop.
"""

raw_names = ["  My Report.TXT ", "Budget 2026 ", " notes DRAFT "]

number = 1
for raw in raw_names:
    clean = raw.strip().lower().replace(" ", "_")
    print(f"{number:02d}_{clean}")
    number = number + 1
# Example output:
# 01_my_report.txt
# 02_budget_2026
# 03_notes_draft
