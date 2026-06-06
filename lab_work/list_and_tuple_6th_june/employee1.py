orders = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("Pen Drive", 600)
]

# Products costing more than 1000
print("Products costing more than ₹1000:")
for product, price in orders:
    if price > 1000:
        print(product, "-", price)

# Most expensive product
max_product = orders[0][0]
max_price = orders[0][1]

for product, price in orders:
    if price > max_price:
        max_price = price
        max_product = product

print("\nMost Expensive Product:", max_product, "-", max_price)

# Total order value
total = 0
for product, price in orders:
    total += price

print("Total Order Value:", total)

# Count products below 1000
count = 0
for product, price in orders:
    if price < 1000:
        count += 1

print("Products costing below ₹1000:", count)