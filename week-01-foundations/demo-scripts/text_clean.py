"""Session 1.4 demo — string methods and f-strings for cleaning text."""

raw = "   joHN   DOE  "

# Common string methods (they return NEW strings; originals are unchanged).
print(raw.strip())            # remove surrounding whitespace
print(raw.strip().title())    # "John   Doe" -> title case
print("hello world".upper())  # HELLO WORLD
print("HELLO".lower())        # hello
print("a,b,c".split(","))     # ['a', 'b', 'c']
print("2024-01".replace("-", "/"))  # 2024/01

# f-strings: embed values directly inside { }
name = raw.strip().title()
price = 3.14159
print(f"Hello, {name}!")
print(f"Price: {price:.2f}")       # 2 decimals -> 3.14
print(f"Padded: {name:>15}")        # right-align in 15 chars
