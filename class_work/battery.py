# Program to display battery percentage after each charging cycle

battery = 20
cycle = 0

while battery < 100:
    cycle += 1
    battery += 10
    print("After Cycle", cycle, "Battery Level =", battery, "%")

print("Battery is fully charged.")