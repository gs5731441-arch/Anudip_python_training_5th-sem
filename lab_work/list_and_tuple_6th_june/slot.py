slots = (1, 0, 1, 1, 0, 0, 1, 0)

occupied = 0
available = 0
available_slots = []

# Count occupied and available slots
for slot in slots:
    if slot == 1:
        occupied += 1
    else:
        available += 1

print("Occupied Slots:", occupied)
print("Available Slots:", available)

# Find first available slot
for i in range(len(slots)):
    if slots[i] == 0:
        print("First Available Slot:", i + 1)
        break

# Store all available slot numbers in a list
for i in range(len(slots)):
    if slots[i] == 0:
        available_slots.append(i + 1)

print("Available Slot Numbers:", available_slots)

# Occupancy percentage
occupancy = (occupied / len(slots)) * 100

print("Occupancy Percentage:", occupancy)

if occupancy > 75:
    print("Parking Occupancy Exceeds 75%")
else:
    print("Parking Occupancy Does Not Exceed 75%")