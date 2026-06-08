units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

# 1. Display houses consuming more than 400 units
print("Houses Consuming More Than 400 Units:")

for house, consumption in units.items():

    if consumption > 400:      # Validation
        print(house)

# 2. Find the highest-consuming house
first = True

for house, consumption in units.items():

    if first == True:
        highest_house = house
        highest_consumption = consumption
        first = False

    elif consumption > highest_consumption:      # Validation
        highest_consumption = consumption
        highest_house = house

print("\nHighest Consumption:")
print(highest_house, "(", highest_consumption, "units )")

# 3. Find the lowest-consuming house
first = True

for house, consumption in units.items():

    if first == True:
        lowest_house = house
        lowest_consumption = consumption
        first = False

    elif consumption < lowest_consumption:      # Validation
        lowest_consumption = consumption
        lowest_house = house

print("\nLowest Consumption:")
print(lowest_house, "(", lowest_consumption, "units )")

# 4. Calculate total units consumed
total_units = 0

for consumption in units.values():

    if consumption >= 0:      # Validation
        total_units += consumption

print("\nTotal Units Consumed =", total_units)

# 5. Create lists
low = []
medium = []
high = []

for house, consumption in units.items():

    if consumption < 200:      # Validation
        low.append(house)

    elif consumption >= 200 and consumption <= 400:      # Validation
        medium.append(house)

    else:      # Validation (consumption > 400)
        high.append(house)

print("\nLow Consumption:", low)
print("Medium Consumption:", medium)
print("High Consumption:", high)

# 6. Count houses eligible for energy-saving campaign
campaign_count = 0

for consumption in units.values():

    if consumption > 300:      # Validation
        campaign_count += 1

print("\nEligible for Energy-Saving Campaign =", campaign_count)