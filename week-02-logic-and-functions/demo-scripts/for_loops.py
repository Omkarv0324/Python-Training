"""Session 2.2 demo — for loops, range(), enumerate()."""

# Loop over a list
colors = ["red", "green", "blue"]
for color in colors:
    print(color)

# range() generates numbers
for i in range(3):
    print("count", i)        # 0, 1, 2

for i in range(2, 11, 2):
    print("even", i)         # 2, 4, 6, 8, 10

# enumerate() gives index + value
for index, color in enumerate(colors, start=1):
    print(index, color)

# Loop over a string
for letter in "hi":
    print(letter)
