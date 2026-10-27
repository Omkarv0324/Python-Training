"""Session 1.3 demo — strings and input()."""

# Strings can use single or double quotes.
first = "Ada"
last = 'Lovelace'

# Concatenation joins strings with +
full_name = first + " " + last
print("Name:", full_name)
print("Length of name:", len(full_name))

# input() ALWAYS returns a string.
name = input("What's your name? ")
print("Hello, " + name + "!")

# To do math on input, convert it with int() or float().
birth_year = int(input("What year were you born? "))
age = 2026 - birth_year
print("You are about", age, "years old.")
