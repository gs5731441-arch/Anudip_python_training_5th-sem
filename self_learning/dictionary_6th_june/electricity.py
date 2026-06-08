units = {
    "House101": 320,
    "House102": 180,
    "House103": 450,
    "House104": 290,
    "House105": 150,
    "House106": 510,
    "House107": 220,
    "House108": 390,
    "House109": 170,
    "House110": 260
}

# 1. Display houses consuming more than 300 units
print("Houses Consuming More Than 300 Units:")

for house, consumption in units.items():

    if consumption > 300:      # Validation
        print(house, ":", consumption)

# 2. Count houses consuming less than 200 units
count = 0

for consumption in units.values():

    if consumption < 200:      # Validation
        count += 1

print("\nHouses Consuming Less Than 200 Units =", count)

# 3. Find the house with the highest consumption
first = True

for house, consumption in units.items():

    if first == True:
        highest_house = house
        highest_consumption = consumption
        first = False

    elif consumption > highest_consumption:      # Validation
        highest_consumption = consumption
        highest_house = house

print("\nHouse with Highest Consumption:")
print(highest_house, ":", highest_consumption)

# 4. Create a list of houses eligible for awareness campaign
campaign_list = []

for house, consumption in units.items():

    if consumption > 400:      # Validation
        campaign_list.append(house)

print("\nHouses Eligible for Awareness Campaign:")
print(campaign_list)

# 5. Categorize houses
print("\nHouse Categories:")

for house, consumption in units.items():

    if consumption < 200:      # Validation
        category = "Low"

    elif consumption >= 200 and consumption <= 350:      # Validation
        category = "Medium"

    else:      # Validation (consumption > 350)
        category = "High"

    print(house, ":", category)