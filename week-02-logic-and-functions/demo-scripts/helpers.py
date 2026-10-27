"""Session 2.5 demo — a reusable helper MODULE.

Import these functions from another script with:  import helpers
Run this file directly to see the self-test below.
"""


def clean_name(raw):
    """Trim, collapse case, and title-case a messy name."""
    return raw.strip().title()


def slugify(text):
    """Turn text into a safe lowercase slug for filenames."""
    return text.strip().lower().replace(" ", "_")


def percent(part, whole):
    """Return part/whole as a percentage rounded to 1 decimal."""
    if whole == 0:
        return 0.0
    return round(part / whole * 100, 1)


# This block only runs when you execute THIS file directly,
# not when it's imported elsewhere.
if __name__ == "__main__":
    print(clean_name("  ada LOVELACE "))
    print(slugify("My Report 2026"))
    print(percent(3, 8))
