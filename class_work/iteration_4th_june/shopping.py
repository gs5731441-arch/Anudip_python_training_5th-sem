# Shopping Cart Bill Calculator

total_bill = 0

while True:
    price = float(input("Enter Item Price: "))

    if price == 0:
        break

    total_bill += price

print("\nTotal Bill Amount: ₹", total_bill)