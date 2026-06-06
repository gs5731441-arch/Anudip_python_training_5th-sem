# Tuple for passenger data
passengers = (12, 18, 25, 30, 28, 15, 8)

# List for stops having fewer than 10 passengers
low_passenger_stops = []

# Busiest stop
max_passengers = passengers[0]
busiest_stop = 1

# Total passengers
total = 0

# Check if any stop exceeded 25 passengers
exceeded_25 = False

for i in range(len(passengers)):

    # Find busiest stop
    if passengers[i] > max_passengers:
        max_passengers = passengers[i]
        busiest_stop = i + 1

    # Stops with fewer than 10 passengers
    if passengers[i] < 10:
        low_passenger_stops.append(i + 1)

    # Total passengers
    total += passengers[i]

    # Exceeded 25 passengers
    if passengers[i] > 25:
        exceeded_25 = True

# Average passengers
average = total / len(passengers)

print("Busiest Stop:", busiest_stop)
print("Passengers at Busiest Stop:", max_passengers)

print("Stops with Fewer Than 10 Passengers:", low_passenger_stops)

print("Average Passengers:", average)

if exceeded_25:
    print("At least one stop exceeded 25 passengers.")
else:
    print("No stop exceeded 25 passengers.")