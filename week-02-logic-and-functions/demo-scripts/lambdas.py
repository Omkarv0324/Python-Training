"""Session 2.5 demo — lambdas (tiny inline functions)."""

# A lambda is a one-line anonymous function.
double = lambda x: x * 2
print(double(10))

# Most useful as a 'key' for sorting.
people = [("Ada", 36), ("Alan", 41), ("Grace", 29)]

by_age = sorted(people, key=lambda person: person[1])
print("By age:", by_age)

by_name = sorted(people, key=lambda person: person[0])
print("By name:", by_name)

# With filter/map (comprehensions are often clearer, but good to recognize)
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda n: n % 2 == 0, nums))
print("Evens:", evens)
