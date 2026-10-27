"""Session 2.5 demo — *args and **kwargs (flexible arguments)."""


def total(*args):
    """Accept any number of positional arguments."""
    print("args is a tuple:", args)
    return sum(args)


print(total(1, 2))
print(total(1, 2, 3, 4, 5))


def describe(**kwargs):
    """Accept any number of keyword arguments."""
    print("kwargs is a dict:", kwargs)
    for key, value in kwargs.items():
        print(f"  {key} = {value}")


describe(name="Ada", role="engineer", team="automation")
