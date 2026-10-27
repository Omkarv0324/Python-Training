"""Session 1.2 automation mini-task — compute an invoice line total with tax."""

item_name = "USB-C cable"
quantity = 4
unit_price = 6.50
tax_rate = 0.08  # 8%

subtotal = quantity * unit_price
tax = subtotal * tax_rate
total = subtotal + tax

print("Item:", item_name)
print("Quantity:", quantity)
print("Subtotal:", subtotal)
print("Tax:", round(tax, 2))
print("Total:", round(total, 2))
