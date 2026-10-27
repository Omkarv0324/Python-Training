"""Session 1.4 automation mini-task — normalize a messy line into a clean log entry."""

raw_line = "  2026-10-27 , WARNING ,   disk almost full  "

# Split on commas, strip each part.
parts = raw_line.split(",")
timestamp = parts[0].strip()
level = parts[1].strip().upper()
message = parts[2].strip().capitalize()

clean = f"[{timestamp}] {level}: {message}"
print(clean)
# -> [2026-10-27] WARNING: Disk almost full
