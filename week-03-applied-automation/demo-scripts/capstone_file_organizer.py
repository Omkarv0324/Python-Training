"""Session 3.5 CAPSTONE — a file organizer.

Sorts files in a target folder into subfolders by file type (extension).
Combines the whole course: pathlib, loops, dicts, functions, error handling, logging.

Usage:
    python capstone_file_organizer.py /path/to/folder
    python capstone_file_organizer.py            # defaults to a self-created demo folder

SAFE BY DEFAULT: with no argument it builds a temporary demo folder with sample
files and organizes that, so it never touches your real files during class.
"""

import logging
import shutil
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger("organizer")

# Map file extensions to destination folder names.
CATEGORIES = {
    "images": {".jpg", ".jpeg", ".png", ".gif"},
    "documents": {".pdf", ".txt", ".md", ".docx"},
    "data": {".csv", ".json", ".xlsx"},
    "archives": {".zip", ".tar", ".gz"},
}


def category_for(suffix):
    """Return the folder name for a given file suffix, or 'other'."""
    suffix = suffix.lower()
    for name, extensions in CATEGORIES.items():
        if suffix in extensions:
            return name
    return "other"


def organize(folder):
    """Move each file in `folder` into a subfolder by category."""
    folder = Path(folder)
    if not folder.exists():
        raise FileNotFoundError(f"Folder does not exist: {folder}")

    moved = 0
    for item in folder.iterdir():
        if item.is_dir():
            continue  # skip folders
        try:
            target_dir = folder / category_for(item.suffix)
            target_dir.mkdir(exist_ok=True)
            shutil.move(str(item), str(target_dir / item.name))
            log.info("Moved %s -> %s/", item.name, target_dir.name)
            moved += 1
        except Exception:
            log.exception("Failed to move %s", item.name)

    log.info("Done. Organized %d file(s).", moved)
    return moved


def build_demo_folder():
    """Create a temporary folder with sample files for a safe demo."""
    demo = Path("demo_messy_folder")
    demo.mkdir(exist_ok=True)
    sample_files = [
        "photo.jpg", "report.pdf", "notes.txt",
        "data.csv", "config.json", "archive.zip", "mystery.xyz",
    ]
    for name in sample_files:
        (demo / name).write_text("sample")
    return demo


def main():
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        log.info("No folder given — creating a safe demo folder.")
        target = build_demo_folder()

    organize(target)


if __name__ == "__main__":
    main()
