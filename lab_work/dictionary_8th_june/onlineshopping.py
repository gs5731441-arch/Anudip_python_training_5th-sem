sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

# 1. Display products sold more than 20 times
print("Products Sold More Than 20 Times:")

for product, count in sales.items():

    if count > 20:      # Validation
        print(product)

# 2. Find the best-selling product
first = True

for product, count in sales.items():

    if first == True:
        best_product = product
        best_sales = count
        first = False

    elif count > best_sales:      # Validation
        best_sales = count
        best_product = product

print("\nBest Selling Product:")
print(best_product, "(", best_sales, ")")

# 3. Find the least-selling product
first = True

for product, count in sales.items():

    if first == True:
        least_product = product
        least_sales = count
        first = False

    elif count < least_sales:      # Validation
        least_sales = count
        least_product = product

print("\nLeast Selling Product:")
print(least_product, "(", least_sales, ")")

# 4. Calculate total products sold
total_sales = 0

for count in sales.values():

    if count >= 0:      # Validation
        total_sales += count

print("\nTotal Units Sold =", total_sales)

# 5. Create list of products requiring promotion
promotion_list = []

for product, count in sales.items():

    if count < 15:      # Validation
        promotion_list.append(product)

print("\nProducts Requiring Promotion:")
print(promotion_list)

# 6. Count products having sales between 10 and 30
sales_count = 0

for count in sales.values():

    if count >= 10 and count <= 30:      # Validation
        sales_count += 1

print("\nProducts Having Sales Between 10 and 30 =", sales_count)