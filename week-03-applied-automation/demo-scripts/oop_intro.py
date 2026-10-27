"""Session 3.5 demo — a gentle intro to classes (OOP)."""


class Task:
    """A simple task with a title and done flag."""

    def __init__(self, title, priority="normal"):
        # __init__ runs when you create a Task. `self` is this instance.
        self.title = title
        self.priority = priority
        self.done = False

    def complete(self):
        self.done = True

    def __str__(self):
        mark = "x" if self.done else " "
        return f"[{mark}] ({self.priority}) {self.title}"


# Create instances (objects)
t1 = Task("Write report", priority="high")
t2 = Task("Water plants")

t1.complete()

for task in [t1, t2]:
    print(task)       # uses __str__
