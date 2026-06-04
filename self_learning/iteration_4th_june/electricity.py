# Electricity Bill Calculation

units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)

else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

# Surcharge
if bill > 5000:
    surcharge = bill * 0.10
else:
    surcharge = 0

final_bill = bill + surcharge

print("Electricity Bill = ₹", bill)
print("Surcharge = ₹", surcharge)
print("Final Payable Amount = ₹", final_bill)