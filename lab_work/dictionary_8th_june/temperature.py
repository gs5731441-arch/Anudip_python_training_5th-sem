temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

# 1. Display cities having temperature above 40°C
print("Cities Above 40°C:")

for city, temp in temperature.items():

    if temp > 40:      # Validation
        print(city)

# 2. Find the hottest city
first = True

for city, temp in temperature.items():

    if first == True:
        hottest_city = city
        highest_temp = temp
        first = False

    elif temp > highest_temp:      # Validation
        highest_temp = temp
        hottest_city = city

print("\nHottest City:")
print(hottest_city, "(", highest_temp, "°C )")

# 3. Find the coolest city
first = True

for city, temp in temperature.items():

    if first == True:
        coolest_city = city
        lowest_temp = temp
        first = False

    elif temp < lowest_temp:      # Validation
        lowest_temp = temp
        coolest_city = city

print("\nCoolest City:")
print(coolest_city, "(", lowest_temp, "°C )")

# 4. Calculate average temperature
total_temp = 0

for temp in temperature.values():

    if temp >= 0:      # Validation
        total_temp += temp

average_temp = total_temp / len(temperature)

print("\nAverage Temperature =", average_temp, "°C")

# 5. Create a list of pleasant cities
pleasant_cities = []

for city, temp in temperature.items():

    if temp < 35:      # Validation
        pleasant_cities.append(city)

print("\nPleasant Cities:")
print(pleasant_cities)

# 6. Count cities with temperature between 35°C and 40°C
count = 0

for temp in temperature.values():

    if temp >= 35 and temp <= 40:      # Validation
        count += 1

print("\nCities Between 35°C and 40°C =", count)