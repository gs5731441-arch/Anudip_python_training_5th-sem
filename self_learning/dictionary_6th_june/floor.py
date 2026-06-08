data = {
    "A": 10,
    "B": 25,
    "C": 40,
    "D": 15,
    "E": 30
}

# Task 1: Display values greater than 20
print("Values Greater Than 20:")

for key, value in data.items():

    if value > 20:      # Validation
        print(key, ":", value)

# Task 2: Count values less than 20
count = 0

for value in data.values():

    if value < 20:      # Validation
        count += 1

print("Count =", count)

# Task 3: Find maximum value
first = True

for key, value in data.items():

    if first == True:
        max_key = key
        max_value = value
        first = False

    elif value > max_value:      # Validation
        max_value = value
        max_key = key

print("Maximum =", max_key, max_value)

# Task 4: Create list
new_list = []

for key, value in data.items():

    if value >= 15 and value <= 35:      # Validation
        new_list.append(key)

print(new_list)

# Task 5: Calculate total
total = 0

for value in data.values():

    if value >= 0:      # Validation
        total += value

print("Total =", total)