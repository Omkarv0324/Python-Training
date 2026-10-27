"""Session 3.4 demo — running external programs with subprocess.

OS-agnostic: we run the Python interpreter itself, which exists everywhere.
"""

import subprocess
import sys

# Run a command and capture its output.
# sys.executable is the path to the current Python — guaranteed to exist.
result = subprocess.run(
    [sys.executable, "--version"],
    capture_output=True,
    text=True,
)

print("Return code:", result.returncode)   # 0 means success
print("stdout:", result.stdout.strip())
print("stderr:", result.stderr.strip())

# Run a tiny inline Python program via -c
result2 = subprocess.run(
    [sys.executable, "-c", "print(6 * 7)"],
    capture_output=True,
    text=True,
)
print("Inline program said:", result2.stdout.strip())
