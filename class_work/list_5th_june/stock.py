stock = [25, 5, 0, 12, 3, 18, 0, 30]

out_stock = 0
available = 0
restock = []
healthy = []

for qty in stock:

    if qty == 0:
        out_stock += 1

    if qty < 10:
        restock.append(qty)

    if qty > 0:
        available += 1

    if qty >= 15:
        healthy.append(qty)

print("Out of Stock Products:", out_stock)
print("Restock Required:", restock)
print("Available Products:", available)
print("Healthy Stock:", healthy)