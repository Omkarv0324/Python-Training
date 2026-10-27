"""Session 4.1 demo — instance attributes vs class attributes."""


class Counter:
    total_counters = 0        # CLASS attribute: shared by all instances

    def __init__(self, name):
        self.name = name      # INSTANCE attribute: unique per object
        self.count = 0
        Counter.total_counters += 1   # update the shared value

    def tick(self):
        self.count += 1


a = Counter("a")
b = Counter("b")
a.tick(); a.tick(); b.tick()

print("a.count:", a.count)             # 2 (per-instance)
print("b.count:", b.count)             # 1 (per-instance)
print("total_counters:", Counter.total_counters)  # 2 (shared)

# Reading a class attribute through an instance works...
print("a sees total:", a.total_counters)   # 2
# ...but assigning through an instance creates a NEW instance attribute (gotcha!):
a.total_counters = 999
print("a shadowed:", a.total_counters)      # 999 (instance)
print("class still:", Counter.total_counters)  # 2 (unchanged)
