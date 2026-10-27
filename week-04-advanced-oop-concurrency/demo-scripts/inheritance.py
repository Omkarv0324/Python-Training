"""Session 4.2 demo — inheritance, overriding, super(), polymorphism."""


class Task:
    def __init__(self, title):
        self.title = title
        self.done = False

    def run(self):
        return f"Running '{self.title}'"

    def complete(self):
        self.done = True


class RetryTask(Task):
    """A Task that remembers how many times to retry."""

    def __init__(self, title, retries=3):
        super().__init__(title)       # run the parent's __init__
        self.retries = retries

    # Override: specialize behavior
    def run(self):
        base = super().run()          # reuse parent behavior
        return f"{base} (will retry up to {self.retries}x)"


class EmailTask(Task):
    def run(self):
        return f"Emailing about '{self.title}'"


# Polymorphism: same loop, different behavior per object type.
tasks = [Task("cleanup"), RetryTask("sync", retries=5), EmailTask("report")]
for t in tasks:
    print(t.run())

r = RetryTask("deploy")
print("Is a Task?", isinstance(r, Task))   # True — subclass "is-a" parent
