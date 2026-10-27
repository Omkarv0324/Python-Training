"""Session 1.3 automation mini-task — generate a standardized filename."""

project = input("Project name: ")
date = input("Date (YYYY-MM-DD): ")

# Lowercase and replace spaces so the filename is clean and consistent.
clean_project = project.strip().lower().replace(" ", "_")

filename = clean_project + "_" + date + ".txt"
print("Suggested filename:", filename)
