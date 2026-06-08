passengers = {
    "Stop1": 12,
    "Stop2": 25,
    "Stop3": 18,
    "Stop4": 32,
    "Stop5": 9,
    "Stop6": 28,
    "Stop7": 14,
    "Stop8": 7,
    "Stop9": 21,
    "Stop10": 16
}

# 1. Display stops having more than 20 passengers
print("Stops Having More Than 20 Passengers:")

for stop, count in passengers.items():

    if count > 20:      # Validation
        print(stop, ":", count)

# 2. Count stops with fewer than 10 passengers
low_count = 0

for count in passengers.values():

    if count < 10:      # Validation
        low_count += 1

print("\nStops with Fewer Than 10 Passengers =", low_count)

# 3. Find the busiest stop
first = True

for stop, count in passengers.items():

    if first == True:
        busiest_stop = stop
        max_passengers = count
        first = False

    elif count > max_passengers:      # Validation
        max_passengers = count
        busiest_stop = stop

print("\nBusiest Stop:")
print(busiest_stop, ":", max_passengers)

# 4. Create a list of stops requiring an extra bus
extra_bus = []

for stop, count in passengers.items():

    if count > 25:      # Validation
        extra_bus.append(stop)

print("\nStops Requiring an Extra Bus:")
print(extra_bus)

# 5. Calculate average number of passengers
total = 0

for count in passengers.values():

    if count >= 0:      # Validation
        total += count

average = total / len(passengers)

print("\nAverage Number of Passengers =", average)