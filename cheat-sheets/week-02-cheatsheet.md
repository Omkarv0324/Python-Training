# Week 2 Cheat Sheet — Logic, Loops & Functions

## Conditions
```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
```

## Operators
```python
==  !=  <  >  <=  >=         # comparison
and   or   not               # logical
# Falsy: 0, 0.0, "", [], {}, set(), None, False
```

## for loops
```python
for item in [1, 2, 3]:
    print(item)

for i in range(5):           # 0..4
    print(i)
range(2, 11, 2)              # 2,4,6,8,10

for i, v in enumerate(items, start=1):
    print(i, v)
```

## while loops
```python
n = 3
while n > 0:
    print(n)
    n -= 1          # change something or loop forever!

break      # exit the loop now
continue   # skip to next iteration
```

## Comprehensions
```python
[x * 2 for x in nums]
[x for x in nums if x % 2 == 0]
{name: len(name) for name in names}
```

## Functions
```python
def area(w, h):
    """Return the area."""
    return w * h

area(3, 4)                    # positional
area(w=3, h=4)                # keyword

def greet(name, greeting="Hello"):   # default param
    return f"{greeting}, {name}!"

# No return -> returns None
```

## Scope
```python
# variables assigned in a function are LOCAL
# use `global x` to modify a module-level variable (sparingly)
```

## Flexible args, lambdas, modules
```python
def total(*args): return sum(args)        # any # of positionals
def opts(**kwargs): return kwargs          # any # of keywords

double = lambda x: x * 2
sorted(people, key=lambda p: p[1])

# reuse code:  import mymodule  then  mymodule.func()
if __name__ == "__main__":
    main()        # runs only when file is executed directly
```
