vehicle = "MH12AB4589"

print("Vehicle Number:", vehicle)

# 1. Extract State Code
state_code = vehicle[:2]
print("State Code:", state_code)

# 2. Extract District Code
district_code = vehicle[2:4]
print("District Code:", district_code)

# 3. Extract Vehicle Series
series = vehicle[4:6]
print("Series:", series)

# 4. Extract Vehicle Number
vehicle_number = vehicle[6:]
print("Vehicle Number:", vehicle_number)

# 5. Count Letters and Digits
letter_count = 0
digit_count = 0

for ch in vehicle:

    if ch.isalpha():
        letter_count += 1

    elif ch.isdigit():
        digit_count += 1

print("\nTotal Letters:", letter_count)
print("Total Digits:", digit_count)

# 6. Validation
valid = True

# First 2 characters must be alphabets
if not vehicle[:2].isalpha():
    valid = False

# Next 2 characters must be digits
if not vehicle[2:4].isdigit():
    valid = False

# Next 2 characters must be alphabets
if not vehicle[4:6].isalpha():
    valid = False

# Last 4 characters must be digits
if not vehicle[6:].isdigit():
    valid = False

# Length should be 10
if len(vehicle) != 10:
    valid = False

# 7. Display Status
if valid:
    print("\nVehicle Number Status: Valid")
else:
    print("\nVehicle Number Status: Invalid")