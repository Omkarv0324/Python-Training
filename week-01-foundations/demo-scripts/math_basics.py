"""Session 1.2 demo — variables, numeric types, and operators."""

# Variables store values. Use clear, snake_case names (PEP 8).
bill_amount = 50.0
tip_percent = 20

# Arithmetic operators
tip = bill_amount * (tip_percent / 100)
total = bill_amount + tip

print("Bill:", bill_amount)
print("Tip:", tip)
print("Total:", total)

# int vs float, and type()
apples = 3            # int
price_each = 0.75     # float
print(type(apples), type(price_each))

# Operator tour
print("Add:", 7 + 2)
print("Subtract:", 7 - 2)
print("Multiply:", 7 * 2)
print("True divide:", 7 / 2)      # 3.5
print("Floor divide:", 7 // 2)    # 3
print("Remainder (modulo):", 7 % 2)  # 1
print("Power:", 7 ** 2)           # 49
