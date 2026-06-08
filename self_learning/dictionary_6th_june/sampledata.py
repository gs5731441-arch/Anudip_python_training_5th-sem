inventory = {
    "Notebook": 45,
    "Pen": 120,
    "Pencil": 80,
    "Eraser": 25,
    "Marker": 15,
    "Stapler": 8,
    "Glue": 12,
    "Scale": 30,
    "Folder": 5,
    "Calculator": 3
}

# 1. Display products with stock less than 10
print("Products with Stock Less Than 10:")

for product, stock in inventory.items():

    if stock < 10:      # Validation
        print(product, ":", stock)

# 2. Count products having stock more than 50
count = 0

for stock in inventory.values():

    if stock > 50:      # Validation
        count += 1

print("\nProducts Having Stock More Than 50 =", count)

# 3. Find the product with minimum stock
first = True

for product, stock in inventory.items():

    if first == True:
        min_product = product
        min_stock = stock
        first = False

    elif stock < min_stock:    # Validation
        min_stock = stock
        min_product = product

print("\nProduct with Minimum Stock:")
print(min_product, ":", min_stock)

# 4. Create a list of products requiring restocking
restock_list = []

for product, stock in inventory.items():

    if stock < 20:      # Validation
        restock_list.append(product)

print("\nProducts Requiring Restocking:")
print(restock_list)

# 5. Calculate total inventory count
total = 0

for stock in inventory.values():

    if stock >= 0:      # Validation
        total += stock

print("\nTotal Inventory Count =", total)